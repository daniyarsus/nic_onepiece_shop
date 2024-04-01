from fastapi import FastAPI
from sqladmin import ModelView

from app.models.payment import Payment


class PaymentAdmin(ModelView, model=Payment):
    column_list = [
        Payment.id,
        Payment.user_id,
        Payment.items_id,
        Payment.amount,
        Payment.currency,
        Payment.status,
        Payment.created_at,
        Payment.updated_at
    ]
