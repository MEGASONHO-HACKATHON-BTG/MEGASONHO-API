from pydantic import BaseModel


class CreateGuestModel(BaseModel):
    name: str
    phone: str
    
    
class GuestModelPayload(BaseModel):
    name: str
    phone: str
    user_uuid: str
    
    
    class Config:
        orm_mode = True