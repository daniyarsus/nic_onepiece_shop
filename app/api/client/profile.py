from typing import Annotated, Union

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form

from app.utils.help.authenticate_user import get_authenticate_user

from app.schemas.profile import ProfileSchema, ProfilePhotoSchema
from app.service.profile import ProfileService
from app.api.dependencies import profile_service
from app.service.getinfobysasha import get_info


router = APIRouter(prefix='/api/v1', tags=['Profile endpoints - API'])


@router.get("/get-info")
def get_info_endpoint(
    payload:dict = Depends(get_authenticate_user)
):
    result = get_info(payload)
    return result


@router.post("/change-photo")
async def set_avatar_endpoint(
        data: ProfilePhotoSchema,
        profiles_service: Annotated[ProfileService, Depends(profile_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await profiles_service.change_photo(data, payload)
    return result


@router.put("/update-profile")
async def update_profile_endpoint(
        data: ProfileSchema,
        profiles_service: Annotated[ProfileService, Depends(profile_service)],
        payload: dict = Depends(get_authenticate_user)
):
    result = await profiles_service.update_profile(data, payload)
    return result


