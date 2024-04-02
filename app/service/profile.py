import os

from typing import Optional

from fastapi import HTTPException, UploadFile
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse

from app.repository.base import AbstractRepository

from app.schemas.profile import ProfileSchema, ProfilePhotoSchema


class ProfileService:
    def __init__(self, profile_repo: AbstractRepository):
        self.profile_repo: AbstractRepository = profile_repo()

    async def get_profile(self, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            profile = await self.profile_repo.get_one(id=payload["id"])

            return JSONResponse(
                content={
                    "id": profile.id,
                    "username": profile.username,
                    "email": profile.email,
                    "phone": profile.phone,
                    "photo": profile.photo
                },
                status_code=200
            )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    async def change_photo(self, data: ProfilePhotoSchema, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            profile_dict = data.dict()
            profile_dict['id'] = payload['id']

            await self.profile_repo.edit_one(
                {
                    'photo': profile_dict['photo']
                },
                id=profile_dict['id']
            )

            return JSONResponse(
                content={
                    "message": "Фотография успешно изменена!"
                },
                status_code=200
            )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    async def update_profile(self, data: ProfileSchema, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            profile_dict = data.dict()
            profile_dict['id'] = payload['id']

            await self.profile_repo.edit_one(
                {
                    'username': profile_dict['username'],
                    'name': profile_dict['name'],
                    'lastname': profile_dict['lastname']
                },
                id=profile_dict['id']
            )

            return JSONResponse(
                content={
                    "message": "Пользователь успешно сменил данные!"
                },
                status_code=200
            )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
