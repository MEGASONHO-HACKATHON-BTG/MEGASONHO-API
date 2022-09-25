from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from typing import List

from src.config.database import get_database

from src.modules.number_lucky.models import NumberLuckyModelPayload

from src.modules.number_lucky.services.create_number_lucky_service import CreateNumberLuckyService
from src.modules.number_lucky.services.list_number_lucky_service import ListNumberLuckyService
from src.modules.number_lucky.services.list_number_lucky_by_user_service import ListNumberLuckysByUserService

router = APIRouter(
    prefix='/number-lucky',
    tags=['Number-lucky']
)

# POST /number-lucky/create
@router.post('/create/', response_model=NumberLuckyModelPayload)
def crate_number_lucky(
    uuid: str = Query(description='uuid do usuário', max_length=36),
    db: Session = Depends(get_database)
):
    service = CreateNumberLuckyService(db)
    return service.execute(uuid)

# GET /number-lucky/list
@router.get('/list/', response_model=List[NumberLuckyModelPayload])
def list_number_lucky(
    filter: bool = Query(None),
    db: Session = Depends(get_database)
):
    service = ListNumberLuckyService(db)
    return service.execute(filter)

# GET /number-lucky/get-by-user
@router.get('/get-by-user/', response_model=List[NumberLuckyModelPayload])
def get_by_user(
    document: str = Query(),
    db: Session = Depends(get_database)
):
    service = ListNumberLuckysByUserService(db)
    return service.execute(document)