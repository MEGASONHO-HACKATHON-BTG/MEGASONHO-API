from pydantic import BaseModel
from typing import Optional

class UserModelPayload(BaseModel):
    uuid: str
    name: str
    document: str
    email: str
    verified_email: Optional[bool]
    phone: str
    verified_phone: Optional[bool]
    is_active: bool


    class Config:
        orm_mode = True

class CreateUserModel(BaseModel):
    name: str
    document: str
    phone: str
    email: str

class UpdateUserModel(CreateUserModel):
    document: Optional[str]