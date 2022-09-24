from sqlalchemy.orm import Session
from src.config.env import env

from src.modules.users.entities.user import User

from src.shared.exceptions.bad_exception import BadRequestException
from src.shared.exceptions.forbidden_exception import ForbiddenException
from src.shared.exceptions.not_found_exception import NotFoundException

from src.modules.users.models import (
  UserModelPayload,
  UpdateUserModel
  )


class UpdateUserService:
  
  def __init__(self, db: Session):
    self._db = db
  
  def execute(self, model: UpdateUserModel, uuid: str, key: str) -> UserModelPayload:
    _key = env.get_item("KEY", None)
    
    if not key:
      raise NotFoundException(message="Chave não encontrada")
    
    if key != _key:
      raise ForbiddenException(message="Sem autorização")
  
    user = self._db.query(User).filter(User.uuid == uuid).first()
    
    if not user:
      raise BadRequestException(message="Usuário não encontrado")
    
    if model.document:
      user.document = model.document

    user.phone = model.phone
    user.name = model.name
    user.email = model.email
    
    self._db.add(user)
    self._db.commit()
    self._db.refresh(user)
    
    return UserModelPayload.from_orm(user)
    