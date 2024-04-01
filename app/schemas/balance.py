from typing import Annotated, Optional, List

from pydantic import BaseModel, Field


class AddBalanceSchema(BaseModel):
    amount: Annotated[float, Field(...)]


class ChangeCardSchema(BaseModel):
    card_number: Annotated[int, Field(ge=1000000000000000, le=9999999999999999)]


class DifferenceBalanceSchema(BaseModel):
    amount: Annotated[float, Field(...)]

