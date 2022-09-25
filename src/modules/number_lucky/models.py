from pydantic import BaseModel
from typing import Optional

from src.modules.users.models import UserModelPayload


class CreateNumberLuckyModel(BaseModel):
    user_uuid: str
    number: str
    is_active: bool


class NumberLuckyModelPayload(BaseModel):
    uuid: str
    user_uuid: str
    user: Optional[UserModelPayload]
    number: str
    is_active: bool


    class Config:
        orm_mode = True