from typing import Annotated, Union

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status

from app.utils.help.authenticate_user import get_authenticate_user

from app.schemas.payment import PaymentSchema
from app.service.payment import PaymentService
from app.api.dependencies import payment_service


router = APIRouter(prefix='/api/v1', tags=['Payment endpoints - API'])


@router.post("/create-payment")
async def create_payment(
        data: PaymentSchema,
        payments_service: Annotated[PaymentService, Depends(payment_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await payments_service.create_payment(data, payload)
    return result


@router.get("/get-all-payments")
async def get_all_payments(
        payments_service: Annotated[PaymentService, Depends(payment_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await payments_service.get_all_payments(payload)
    return result

