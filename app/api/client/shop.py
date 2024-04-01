from typing import Annotated, Union

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status

from app.service.product import ProductService
from app.schemas.product import ProductCalculateSchema
from app.api.dependencies import product_service


router = APIRouter(prefix='/api/v1', tags=['Product endpoints - API'])


@router.get("/get-all-products")
async def get_all_products_endpoint(
        products_service: Annotated[ProductService, Depends(product_service)]
):
    result = await products_service.get_all_products()
    return result


@router.get("/get-product-by-id/{product_id}")
async def get_product_by_id_endpoint(
        product_id: int,
        products_service: Annotated[ProductService, Depends(product_service)]
):
    result = await products_service.get_product_by_id(product_id)
    return result


@router.post("/calculate-price")
async def calculate_price_endpoint(
        items_id: ProductCalculateSchema,
        products_service: Annotated[ProductService, Depends(product_service)]
):
    result = await products_service.get_calculate_price(items_id)
    return result
