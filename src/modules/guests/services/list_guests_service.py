from sqlalchemy.orm import Session

from src.modules.guests.entities.guest import Guest

from src.modules.guests.models import GuestModelPayload

from src.shared.exceptions.bad_exception import BadRequestException


class ListGuestsService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self) -> GuestModelPayload:
      guests = self._db.query(Guest).all()

      return [GuestModelPayload.from_orm(guest) for guest in guests]