from typing import List
from urllib import response
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.config.database import get_database

from src.modules.guests.models import (
  CreateGuestModel,
  GuestModelPayload
)

from src.modules.guests.services.list_guests_by_user import ListGuestsByUserService
from src.modules.guests.services.list_guests_service import ListGuestsService
from src.modules.guests.services.create_guest_service import CreateGuestService

router = APIRouter(
    prefix='/guests',
    tags=['Guest']
)

# POST /guests/create
@router.post('/create/', response_model=GuestModelPayload)
def create_guest(
    model: CreateGuestModel,
    document: str = Query(),
    db: Session = Depends(get_database)
):
    service = CreateGuestService(db)
    return service.execute(model, document)

# GET /guests/list
@router.get('/list/', response_model=List[GuestModelPayload])
def list_users(
    db: Session = Depends(get_database)
):
    service = ListGuestsService(db)
    return service.execute()

# GET /guests/get-by-user
@router.get('/get-by-user/', response_model=List[GuestModelPayload])
def get_by_user(
    document: str = Query(),
    db: Session = Depends(get_database)
):
    service = ListGuestsByUserService(db)
    return service.execute(document)