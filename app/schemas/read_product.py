from pydantic import BaseModel
from typing import Optional


class ReadProductModel(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    currency: str
    type: str
    status: bool
