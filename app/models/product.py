from datetime import datetime, timedelta

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.settings.db.connection import Base

from app.schemas.read_product import ReadProductModel


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    currency: Mapped[str] = mapped_column(default="belly")
    type: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_read_model(self) -> ReadProductModel:
        """
        Преобразует объект продукта в ReadProductModel
        """
        return ReadProductModel(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price,
            currency=self.currency,
            type=self.type,
            status=self.status
        )
