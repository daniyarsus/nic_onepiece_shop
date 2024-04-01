from typing import List

from app.models.product import Product

from app.repository.base import AbstractRepository

from app.schemas.product import ProductCalculateSchema


class ProductService:
    def __init__(self, products_repo: AbstractRepository):
        self.products_repo: AbstractRepository = products_repo()

    async def get_all_products(self) -> List[dict]:
        try:
            all_products = await self.products_repo.get_all()
            return [
                {'id': product.id,
                 'name': product.name,
                 'description': product.description,
                 'price': product.price,
                 'currency': product.currency,
                 'type': product.type}
                for product in all_products
                ]
        except Exception as e:
            raise e

    async def get_product_by_id(self, product_id: int) -> dict:
        try:
            product = await self.products_repo.get_one(product_id)
            return {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'currency': product.currency,
                'type': product.type
            }
        except Exception as e:
            raise e

    async def get_calculate_price(self, data: ProductCalculateSchema):
        total_price = 0
        try:
            for item_id in data.items_id:
                product = await self.products_repo.get_one(id=item_id)
                total_price += product.price
            return {'total_price': total_price}
        except Exception as e:
            raise e
