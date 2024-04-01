from typing import Optional

from fastapi import HTTPException

from fastapi.responses import JSONResponse

from app.repository.base import AbstractRepository
from app.schemas.balance import AddBalanceSchema, ChangeCardSchema, DifferenceBalanceSchema


class BalanceService:
    def __init__(self, balance_repo: AbstractRepository):
        self.balance_repo: AbstractRepository = balance_repo()

    async def change_balance(self, data: AddBalanceSchema, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            balance_dict = data.dict()
            balance_dict["id"] = int(payload["id"])

            belly = balance_dict['amount'] * 100000

            user_record = await self.balance_repo.get_one(id=balance_dict["id"])

            user_balance = user_record.balance

            new_balance = belly + user_balance

            result = await self.balance_repo.edit_one({"balance": new_balance}, id=payload["id"])

            return result

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    async def change_card(self, data: ChangeCardSchema, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            balance_dict = data.dict()
            balance_dict["id"] = int(payload["id"])

            result = await self.balance_repo.update_one(balance_dict)
            return result

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    async def get_balance(self, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            balance = await self.balance_repo.get_one(id=payload["id"])

            user_balance = balance.balance

            return user_balance

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    async def get_difference_balance(self, data: DifferenceBalanceSchema, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            balance_dict = data.dict()
            balance_dict["id"] = int(payload["id"])

            user_record = await self.balance_repo.get_one(id=balance_dict["id"])

            # Получаем баланс пользователя из записи о балансе.
            user_balance = user_record.balance

            # Вычисляем разницу между текущим балансом пользователя и балансом, предоставленным в balance_dict.
            difference = user_balance - balance_dict["amount"]

            if difference < 0:
                raise HTTPException(
                    status_code=400,
                    detail="Недостаточно средств на счету!"
                )

            user_update = await self.balance_repo.edit_one({"balance": difference}, id=payload["id"])

            return user_update

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

