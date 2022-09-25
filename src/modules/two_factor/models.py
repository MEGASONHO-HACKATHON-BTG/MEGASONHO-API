from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class TwoFactorType(Enum):
    WHATSAPP = 'WHATSAPP'


class CreateTwoFactorModel(BaseModel):
    user_uuid: str
    two_factor_type: TwoFactorType

    expires_at: Optional[datetime]
    expires_hours: Optional[int]
    code: Optional[str]
    token: Optional[str]

    class Config:
        use_enum_values = True


class TwoFactorModel(BaseModel):
    id: Optional[int]
    user_uuid: str
    code: str
    token: str
    two_factor_type: str
    expires_hours: int
    expires_at: datetime
    validated_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ActivateTwoFactorModel(BaseModel):
    code: str
    token: str