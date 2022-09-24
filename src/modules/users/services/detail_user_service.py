from sqlalchemy.orm import Session
from src.config.env import env

from src.modules.users.models import UserModelPayload
from src.modules.users.entities.user import User

from src.shared.exceptions.bad_exception import BadRequestException
from src.shared.exceptions.forbidden_exception import ForbiddenException
from src.shared.exceptions.not_found_exception import NotFoundException


class DetailUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, document: str, key: str) -> UserModelPayload:
        _key = env.get_item("KEY", None)
    
        if not key:
            raise NotFoundException(message="Chave não encontrada")
    
        if key != _key:
            raise ForbiddenException(message="Sem autorização")
  
        user = self._db.query(User).filter(User.document == document).first()

        if not user:
            raise BadRequestException(message='Usuário não encontrado')

        return UserModelPayload.from_orm(user)