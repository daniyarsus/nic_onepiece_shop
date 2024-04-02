from pydantic import BaseModel
from typing import Optional, List


class ReadProductModel(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    currency: str
    type: str
    status: bool
    photo: List[str]

    class Config:
        from_attributes = True
