from typing import List

from datetime import datetime, timedelta

from pydantic import BaseModel


class ReadPaymentModel(BaseModel):
    id: int
    user_id: int
    items_id: List[int]
    amount: float
    currency: str
    place: str
    status: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
