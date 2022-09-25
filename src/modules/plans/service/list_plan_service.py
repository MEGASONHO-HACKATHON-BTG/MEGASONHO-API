from typing import List
from sqlalchemy.orm import Session

from src.modules.plans.entities.plans import Plans
from src.modules.plans.models import PlanPayloadModel


class ListPlanService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self) -> List[PlanPayloadModel]:

        plans = self._db.query(Plans).all()
    
        return [PlanPayloadModel.from_orm(plan) for plan in plans]
