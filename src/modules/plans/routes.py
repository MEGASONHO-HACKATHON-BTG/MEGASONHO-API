from typing import List
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from src.config.database import get_database

from src.modules.plans.models import CreatePlanModel, PlanPayloadModel

from src.modules.plans.service.create_plan_service import CreatePlanService
from src.modules.plans.service.list_plan_service import ListPlanService
from src.modules.plans.service.purchase_plan_service import PurchasePlanService

router = APIRouter(
    prefix='/plans',
    tags=['Plans']
)

@router.post('/create/', response_model=PlanPayloadModel)
def create_plan(
    model: CreatePlanModel,
    db: Session = Depends(get_database)
):
    service = CreatePlanService(db)
    return service.execute(model)

@router.get('/list/', response_model=List[PlanPayloadModel])
def list_plan(
    db: Session = Depends(get_database)
):
    service = ListPlanService(db)
    return service.execute()

@router.post('/purchase/', response_model=bool)
def purchase_plan(
    document: str = Query(),
    uuid: str = Query(),
    db: Session = Depends(get_database)
):
    service = PurchasePlanService(db)
    return service.execute(uuid, document)