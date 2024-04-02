from typing import Annotated, Optional

from pydantic import Field, BaseModel


class ProfileSchema(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
