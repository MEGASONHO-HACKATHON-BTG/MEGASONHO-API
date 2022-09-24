from typing import List
from sqlalchemy.orm import Session
from src.config.env import env

from src.modules.users.models import UserModelPayload
from src.modules.users.entities.user import User

from src.shared.exceptions.forbidden_exception import ForbiddenException
from src.shared.exceptions.not_found_exception import NotFoundException


class ListUsersService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, key: str) -> List[UserModelPayload]:
        _key = env.get_item("KEY", None)
    
        if not key:
            raise NotFoundException(message="Chave não encontrada")
    
        if key != _key:
            raise ForbiddenException(message="Sem autorização")
  
        users = self._db.query(User).all()

        return [UserModelPayload.from_orm(user) for user in users]