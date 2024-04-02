from typing import Annotated, Union

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form

from app.utils.help.authenticate_user import get_authenticate_user

from app.schemas.profile import ProfileSchema
from app.service.profile import ProfileService
from app.api.dependencies import profile_service


router = APIRouter(prefix='/api/v1', tags=['Profile endpoints - API'])


@router.get("/get-info")
async def get_info_endpoint(
        profiles_service: Annotated[ProfileService, Depends(profile_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await profiles_service.get_profile(payload)
    return result


@router.post("/set-avatar")
async def set_avatar_endpoint(
        profiles_service: Annotated[ProfileService, Depends(profile_service)],
        data: UploadFile = File(...),
        payload: dict = Depends(get_authenticate_user)
):
    result = await profiles_service.set_avatar(data, payload)
    return result


@router.get("/get-avatar")
async def get_avatar_endpoint(
        profiles_service: Annotated[ProfileService, Depends(profile_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await profiles_service.get_avatar(payload)
    return result


@router.put("/update-profile")
async def update_profile_endpoint(
        data: ProfileSchema,
        profiles_service: Annotated[ProfileService, Depends(profile_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await profiles_service.update_profile(data, payload)
    return result
