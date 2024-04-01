from fastapi import FastAPI
from sqladmin import ModelView

from app.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.username,
        User.password,
        User.email,
        User.phone,
        User.name,
        User.lastname,
        User.card_number,
        User.balance,
        User.is_verified,
        User.role,
        User.created_at,
        User.updated_at
    ]
