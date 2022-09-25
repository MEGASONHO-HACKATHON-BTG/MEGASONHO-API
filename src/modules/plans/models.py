from datetime import date
from typing import Optional
from pydantic import BaseModel


class CreatePlanModel(BaseModel):
    quantity: int
    price: int


class PlanPayloadModel(CreatePlanModel):
    uuid: str
    created_at: Optional[date]
    updated_at: Optional[date]


    class Config:
        orm_mode = True