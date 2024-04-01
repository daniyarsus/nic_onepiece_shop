from typing import Annotated, Optional, List

from pydantic import BaseModel, Field


class PaymentSchema(BaseModel):
    items_id: Annotated[List[int], Field(...)]
    place: Optional[Annotated[str, Field(...)]] = None
