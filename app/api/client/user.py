from typing import Annotated, Union

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status

from app.utils.help.authenticate_user import get_authenticate_user

from app.schemas.balance import AddBalanceSchema, ChangeCardSchema, DifferenceBalanceSchema
from app.service.balance import BalanceService
from app.api.dependencies import balance_service


router = APIRouter(prefix='/api/v1', tags=['User endpoints - API'])


@router.put("/change-balance")
async def change_balance_endpoint(
        data: AddBalanceSchema,
        balances_service: Annotated[BalanceService, Depends(balance_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await balances_service.change_balance(data, payload)
    return result


@router.put("/change-card")
async def change_card_endpoint(
        data: ChangeCardSchema,
        balances_service: Annotated[BalanceService, Depends(balance_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await balances_service.change_card(data, payload)
    return result


@router.get("/get-balance")
async def get_balance_endpoint(
        balances_service: Annotated[BalanceService, Depends(balance_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await balances_service.get_balance(payload)
    return result


@router.post("/get-difference-balance")
async def get_difference_balance_endpoint(
        data: DifferenceBalanceSchema,
        balances_service: Annotated[BalanceService, Depends(balance_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await balances_service.get_difference_balance(data, payload)
    return result
