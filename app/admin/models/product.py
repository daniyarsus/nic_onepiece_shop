from fastapi import FastAPI
from sqladmin import ModelView

from app.models.product import Product


class ProductAdmin(ModelView, model=Product):
    column_list = [
        Product.id,
        Product.name,
        Product.description,
        Product.price,
        Product.currency,
        Product.status,
        Product.created_at,
        Product.updated_at
    ]

