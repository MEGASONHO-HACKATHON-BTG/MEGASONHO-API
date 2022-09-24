from uuid import uuid4
from sqlalchemy.orm import Session

from src.modules.plans.entities.plans import Plans
from src.modules.plans.models import CreatePlanModel, PlanPayloadModel


class CreatePlanService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, model: CreatePlanModel) -> PlanPayloadModel:
        db_plan = Plans(**model.dict())
        db_plan.uuid = str(uuid4())

        self._db.add(db_plan)
        self._db.commit()
        self._db.refresh(db_plan)
    
        return PlanPayloadModel.from_orm(db_plan)
