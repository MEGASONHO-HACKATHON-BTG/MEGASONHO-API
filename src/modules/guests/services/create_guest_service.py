from typing import List
from uuid import uuid4
from random import randrange
from sqlalchemy.orm import Session

from src.modules.guests.entities.guest import Guest
from src.modules.users.entities.user import User

from src.modules.guests.models import ( 
    CreateGuestModel,
    GuestModelPayload
)

from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.bad_exception import BadRequestException

from src.shared.services.bot_conversa import BotConversaApi


class CreateGuestService:

    def __init__(self, db: Session):
        self._db = db
        self._whatsapp_api = BotConversaApi()
    
    def execute(self, model: List[CreateGuestModel], document: str) -> List[GuestModelPayload]:
        
        if len(model) > 3:
            raise BadRequestException(message="Usuário já contém o número máximo de convidados")

        user = self._db.query(User).filter(User.document == document).first()
        
        if not user:
            raise NotFoundException(message="Usuário não encontrado")
        
        guests = self._db.query(Guest).filter(Guest.user_uuid == user.uuid).all()
        
        if len(guests) > 2:
            raise BadRequestException(message="Número máximo de convidados já cadastrado")
    
        code = str(randrange(100_000, 999_999))

        guests = []
        
        i = 0
        
        for payload in model:
            db_guest = Guest(**payload.dict())
            db_guest.uuid = str(uuid4())
            db_guest.user_uuid = user.uuid

            subscriber = self._whatsapp_api.check_subscriber(model.phone)

            if subscriber == 404:
                name = model.name.split(' ')
                first_name = name[0]
                last_name = name[1]

                self._whatsapp_api.subscriber(model.phone, first_name, last_name)

                get_subscriber = self._whatsapp_api.find_subscriber(model.phone)

                self._whatsapp_api.send_mensage(get_subscriber, code)
            
            get_subscriber = self._whatsapp_api.find_subscriber(model.phone)

            self._whatsapp_api.send_mensage(get_subscriber, code)

            self._db.add(db_guest)
            self._db.commit()
            self._db.refresh(db_guest)

            guests.append(db_guest)
            i += 1
            
        user.code = code
        user.max_use = i
        
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)

        return [GuestModelPayload.from_orm(guest) for guest in guests] 