from app.repository.base import SQLAlchemyRepository

from app.models.payment import Payment


class PaymentRepository(SQLAlchemyRepository):
    model = Payment
