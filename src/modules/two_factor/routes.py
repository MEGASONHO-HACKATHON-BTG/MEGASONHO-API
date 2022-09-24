from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_database

from src.modules.two_factor.models import TwoFactorModel, ActivateTwoFactorModel, CreateTwoFactorModel

from src.modules.two_factor.services.create_two_factor_service import CreateTwoFactorService
from src.modules.two_factor.services.active_two_factor_service import ActivateTwoFactorService

router = APIRouter(
    prefix='/two-factor',
    tags=['Two-factor']
)

# POST /two-factor/create/
@router.post('/create/', response_model=TwoFactorModel)
def create_two_factor(
    model: CreateTwoFactorModel,
    db: Session = Depends(get_database)
):
    service = CreateTwoFactorService(db)
    return service.execute(model)

# POST /two-factor/activate
@router.post('/activate/', response_model=TwoFactorModel)
def activate_two_factor(
    model: ActivateTwoFactorModel,
    db: Session = Depends(get_database)
):
    service = ActivateTwoFactorService(db)
    return service.execute(model)