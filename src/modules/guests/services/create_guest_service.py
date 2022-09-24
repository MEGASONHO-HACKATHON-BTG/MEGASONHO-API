from sqlalchemy.orm import Session

from src.modules.users.entities.user import User

from src.modules.guests.models import CreateGuestModel

from src.shared.exceptions.not_found_exception import NotFoundException

class CreateGuestService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, model: CreateGuestModel, uuid: str):
        pass