from datetime import datetime, timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.settings.db.connection import Base

from app.schemas.read_payment import ReadPaymentModel


class Payment(Base):
    __tablename__ = 'payments'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    amount: Mapped[bool] = mapped_column(nullable=False)
    currency: Mapped[str] = mapped_column(default='KZT')
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    async def delete_unverified_payments(cls, session):
        """
        Удаляет всех пользователей, которые не подтвердили свою учетную запись в течение 7 дней.
        """
        seven_days_ago = datetime.utcnow() - timedelta(days=7)
        unverified_payments = session.query(cls).filter(cls.is_verified == False,
                                                        cls.created_at <= seven_days_ago).all()
        for payment in unverified_payments:
            session.delete(payment)
        await session.commit()

    def to_read_model(self) -> ReadPaymentModel:
        """
        Преобразует объект платежа в ReadPaymentModel
        """
        return ReadPaymentModel(
            id=self.id,
            amount=self.amount,
            currency=self.currency,
            status=self.status
        )
