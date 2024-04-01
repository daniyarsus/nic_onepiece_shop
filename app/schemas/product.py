from typing import Annotated, Optional, List

from pydantic import BaseModel, Field


class ProductCalculateSchema(BaseModel):
    items_id: Annotated[List[int], Field(...)]
