from uuid import uuid4
from sqlalchemy.orm import Session
from src.config.env import env

from src.modules.users.entities.user import User

from src.modules.users.models import CreateUserModel, UserModelPayload

from src.shared.exceptions.bad_exception import BadRequestException

from src.modules.number_lucky.services.create_number_lucky_service import CreateNumberLuckyService

from src.shared.services.bot_conversa import BotConversaApi


class CreateUserService:

    def __init__(self, db: Session):
        self._db = db
        self._whatsapp_api = BotConversaApi()
    
    def execute(self, model: CreateUserModel, code: str) -> UserModelPayload:
        user = self._db.query(User).filter(User.code == code).first()
        
        if user: 
            if code and user.max_use > 0:
                service = CreateNumberLuckyService(self._db)

                service.execute(user.uuid)
                user.max_use -= 1
                
                self._db.add(user)
                self._db.commit()
                self._db.refresh(user)
            elif user.max_use == 0:
                raise BadRequestException(message='O usuário já resgatou o número máximo de números da sorte com convidados')

        if len(model.document) > 11:
            raise BadRequestException(message='Tamanho máximo de documento 11 digitos')
        
        user_document = self._db.query(User).filter(User.document == model.document).first()

        if user_document:
            raise BadRequestException(message='Documento já cadastrado')
        
        user_name = self._db.query(User).filter(User.name == model.name).first()

        if user_name:
            raise BadRequestException(message='Nome de usuário já cadastrado')

        user_phone = self._db.query(User).filter(User.phone == model.phone).first()

        if user_phone:
            raise BadRequestException(message='Telefone já cadastrado')
        
        user_email = self._db.query(User).filter(User.email == model.email).first()

        if user_email:
            raise BadRequestException(message='E-mail já cadastrado')
        
        subscriber = self._whatsapp_api.check_subscriber(model.phone)

        if subscriber == 404:
            name = model.name.split(' ')
            first_name = name[0]
            last_name = name[1]

            self._whatsapp_api.subscriber(model.phone, first_name, last_name)

        db_user = User(**model.dict())
        db_user.uuid = str(uuid4())

        self._db.add(db_user)
        self._db.commit()
        self._db.refresh(db_user)

        return UserModelPayload.from_orm(db_user)