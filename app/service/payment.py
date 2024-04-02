from typing import Optional, List, Dict

import httpx

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.settings.config import settings

from app.settings.redis.connection import redis_client_auth

from app.repository.base import AbstractRepository

from app.schemas.payment import PaymentSchema


class PaymentService:
    def __init__(self, payments_repo: AbstractRepository):
        self.payment_repo: AbstractRepository = payments_repo()

    async def create_payment(self, data: PaymentSchema, payload: Dict[str, str]) -> Optional[JSONResponse | HTTPException]:
        try:
            payment_dict = data.dict()
            payment_dict['user_id'] = int(payload['id'])

            calculate_price_url = f"{settings.host_config.HOST}/api/v1/calculate-price"

            async with httpx.AsyncClient() as client:
                calculate_price_response = await client.post(
                    calculate_price_url,
                    json={"items_id": payment_dict["items_id"]}
                )

            if calculate_price_response.status_code != 200:
                raise HTTPException(
                    status_code=calculate_price_response.status_code,
                    detail=calculate_price_response.text
                )

            total_price = calculate_price_response.json()["total_price"]

            payment_dict["items_id"] = data.items_id
            payment_dict["amount"] = total_price
            payment_dict["place"] = data.place
            # ToDo - add payment status functionality
            payment_dict["status"] = True

            payload_id = str(payload['id'])
            payload_session_id = payload['session_id']

            jwt = await redis_client_auth.get(f"jwt_user_id:{payload_id}_session_id:{payload_session_id}")
            jwt = jwt.decode("utf-8")

            get_difference_balance_url = f"{settings.host_config.HOST}/api/v1/get-difference-balance"

            async with httpx.AsyncClient() as client:
                get_difference_balance_response = await client.post(
                    get_difference_balance_url,
                    json={"amount": total_price},
                    headers={"Authorization": f"Bearer {jwt}"}
                )

            if get_difference_balance_response.status_code != 200:
                raise HTTPException(
                    status_code=get_difference_balance_response.status_code,
                    detail=get_difference_balance_response.text
                )

            result = await self.payment_repo.add_one(payment_dict)
            return result

        except Exception as e:
            raise e

    async def get_all_payments(self, payload: Dict[str, str]) -> Optional[List[Dict[str, str]]]:
        try:
            all_payments = await self.payment_repo.get_all(user_id=payload['id'])
            return [
                {'id': payment.id,
                 'items_id': payment.items_id,
                 'amount': payment.amount,
                 'place': payment.place,
                 'created_at': payment.created_at}
                for payment in all_payments
            ]
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )


async def serialize_response(response_content):
    content = await response_content
    return jsonable_encoder(content)
