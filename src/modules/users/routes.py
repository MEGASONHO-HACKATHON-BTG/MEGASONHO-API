from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.config.database import get_database

from src.modules.users.models import (
    CreateUserModel,
    UpdateUserModel,
    UserModelPayload
)

from src.modules.users.services.create_user_service import CreateUserService
from src.modules.users.services.list_users_service import ListUsersService
from src.modules.users.services.delete_user_service import DeleteUserService
from src.modules.users.services.update_user_service import UpdateUserService
from src.modules.users.services.get_user_by_document_service import GetUserByDocumentService
from src.modules.users.services.detail_user_service import DetailUserService

router = APIRouter(
    prefix='/users',
    tags=['User']
)

# POST /users/create
@router.post('/create/', response_model=UserModelPayload)
def create_user(
    model: CreateUserModel,
    db: Session = Depends(get_database)
):
    service = CreateUserService(db)
    return service.execute(model)

# GET /users/check-document/{document}
@router.get('/check-document/', response_model=bool)
def check_document(
    document: str = Query(max_length=11),
    db: Session = Depends(get_database)
):
    service = GetUserByDocumentService(db)
    return service.execute(document)

# GET /users/detail/{document}
@router.get('/detail/', response_model=UserModelPayload)
def check_document(
    key: str = Query(),
    document: str = Query(max_length=11),
    db: Session = Depends(get_database)
):
    service = DetailUserService(db)
    return service.execute(document, key)

# GET /users/list
@router.get('/list/', response_model=List[UserModelPayload])
def list_users(
    key: str = Query(),
    db: Session = Depends(get_database)
):
    service = ListUsersService(db)
    return service.execute(key)

# DELETE /users/delete/{uuid}
@router.delete('/delete/', response_model=bool)
def delete_user(
    uuid: str = Query(max_length=36),
    key: str = Query(),
    db: Session = Depends(get_database)
):
    service = DeleteUserService(db)
    return service.execute(uuid, key)

# UPDATE /users/update/{uuid}
@router.put("/update/", response_model=UserModelPayload)
def update_user(
    model: UpdateUserModel,
    uuid: str = Query(max_length=36),
    key: str = Query(),
    db: Session = Depends(get_database)
):
    service = UpdateUserService(db)
    return service.execute(model, uuid, key)