from app.repository.base import SQLAlchemyRepository

from app.models.product import Product


class ProductRepository(SQLAlchemyRepository):
    model = Product
