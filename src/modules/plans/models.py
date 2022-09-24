from datetime import date
from typing import Optional
from pydantic import BaseModel


class CreatePlanModel(BaseModel):
    quantity: int
    price: int


class PlanPayloadModel(CreatePlanModel):
    uuid: str
    create_at: Optional[date]
    update_at: Optional[date]

    class Config:
        orm_mode = True