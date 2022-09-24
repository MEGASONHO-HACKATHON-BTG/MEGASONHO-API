from uuid import uuid4
from sqlalchemy.orm import Session

from src.modules.guests.entities.guest import Guest
from src.modules.users.entities.user import User

from src.modules.guests.models import ( 
    CreateGuestModel,
    GuestModelPayload
)

from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.bad_exception import BadRequestException

class CreateGuestService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, model: CreateGuestModel, document: str) -> GuestModelPayload:
        user = self._db.query(User).filter(User.document == document).first()
        
        if not user:
            raise NotFoundException(message="Usuário não encontrado")
        
        guests = self._db.query(Guest).filter(Guest.user_uuid == user.uuid).all()
        
        if (len(guests) > 2):
            raise BadRequestException(message="Número máximo de convidados já cadastrado")
        
        db_guest = Guest(**model.dict())
        db_guest.uuid = str(uuid4())
        db_guest.user_uuid = user.uuid
        
        self._db.add(db_guest)
        self._db.commit()
        self._db.refresh(db_guest)

        return GuestModelPayload.from_orm(db_guest)