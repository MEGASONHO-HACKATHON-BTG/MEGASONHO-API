from pydantic import BaseModel


class CreateGuestModel(BaseModel):
    name: str
    phone: str