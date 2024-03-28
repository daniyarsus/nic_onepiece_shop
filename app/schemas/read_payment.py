from pydantic import BaseModel


class ReadPaymentModel(BaseModel):
    id: int
    amount: float
    currency: str
    status: str
