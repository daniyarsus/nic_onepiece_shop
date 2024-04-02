import os

from typing import Optional

from fastapi import HTTPException, UploadFile
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse

from app.repository.base import AbstractRepository

from app.schemas.profile import ProfileSchema


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
                    "phone": profile.phone
                },
                status_code=200
            )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    async def set_avatar(self, data: UploadFile, payload: dict) -> Optional[JSONResponse | HTTPException]:
        user_dir = f"media/user/{payload['id']}"
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)

        data.filename = "avatar.jpg"
        with open(f"media/user/{payload['id']}/{data.filename}", "wb") as buffer:
            buffer.write(data.file.read())

        return JSONResponse(
            content={
                "message": "Аватар успешно установлен!"
            },
            status_code=200
        )

    async def get_avatar(self, payload: dict) -> Optional[JSONResponse | HTTPException]:
        return FileResponse(f"media/user/{payload['id']}/avatar.jpg", media_type="image/jpeg")

    async def update_profile(self, data: ProfileSchema, payload: dict) -> Optional[JSONResponse | HTTPException]:
        try:
            profile_dict = data.dict()
            profile_dict['id'] = payload['id']

            result = await self.profile_repo.edit_one(
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
