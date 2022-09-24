from sqlalchemy.orm import Session

from src.modules.guests.entities.guest import Guest
from src.modules.users.entities.user import User

from src.modules.guests.models import ( 
    GuestModelPayload
)

from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.bad_exception import BadRequestException

class ListGuestsByUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, document: str) -> GuestModelPayload:
      user = self._db.query(User).filter(User.document == document).first()
      
      if not user:
            raise NotFoundException(message="Usuário não encontrado")
        
      guests = self._db.query(Guest).filter(Guest.user_uuid == user.uuid).all()
      
      return [GuestModelPayload.from_orm(guest) for guest in guests]