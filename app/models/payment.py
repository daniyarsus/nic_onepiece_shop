from datetime import datetime, timedelta

from sqlalchemy import ForeignKey, Column, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY

from app.settings.db.connection import Base

from app.schemas.read_payment import ReadPaymentModel


class Payment(Base):
    __tablename__ = 'payments'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    items_id: Mapped[list] = mapped_column(ARRAY(Integer), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    currency: Mapped[str] = mapped_column(default="belly")
    place: Mapped[str] = mapped_column(default="Kazakhstan, Almaty")
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_read_model(self) -> ReadPaymentModel:
        """
        Преобразует объект платежа в ReadPaymentModel
        """
        return ReadPaymentModel(
            id=self.id,
            user_id=self.user_id,
            items_id=self.items_id,
            amount=self.amount,
            place=self.place,
            currency=self.currency,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
