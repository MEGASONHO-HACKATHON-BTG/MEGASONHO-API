from sqlalchemy.orm import Session

from src.modules.number_lucky.entities.number_lucky import NumberLucky
from src.modules.users.entities.user import User

from src.modules.number_lucky.models import NumberLuckyModelPayload

from src.shared.exceptions.not_found_exception import NotFoundException


class ListNumberLuckysByUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, document: str) -> NumberLuckyModelPayload:
      user = self._db.query(User).filter(User.document == document).first()
      print(user)
      
      if not user:
            raise NotFoundException(message="Usuário não encontrado")
        
      number_luckys = self._db.query(NumberLucky).filter(NumberLucky.user_uuid == user.uuid).all()
      
      return [NumberLuckyModelPayload.from_orm(numberlucky) for numberlucky in number_luckys]