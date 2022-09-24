from sqlalchemy.orm import Session
from src.config.env import env

from src.modules.users.entities.user import User

from src.shared.exceptions.bad_exception import BadRequestException
from src.shared.exceptions.forbidden_exception import ForbiddenException
from src.shared.exceptions.not_found_exception import NotFoundException


class DeleteUserService:

  def __init__(self, db: Session):
    self._db = db
  
  def execute(self, uuid: str, key: str) -> bool:
    _key = env.get_item("KEY", None)
    
    if not key:
      raise NotFoundException(message="Chave não encontrada")
    
    if key != _key:
      raise ForbiddenException(message="Sem autorização")
    
    user = self._db.query(User).filter(User.uuid == uuid).first()

    if not user:
      raise BadRequestException(message="Usuário não encontrado")

    self._db.query(User).filter(User.uuid == uuid).delete()
    
    self._db.commit()
    
    return True
