from uuid import uuid4
from random import randrange
from sqlalchemy.orm import Session

from src.modules.users.entities.user import User

from src.modules.number_lucky.entities.number_lucky import NumberLucky
from src.modules.number_lucky.models import CreateNumberLuckyModel, NumberLuckyModelPayload

from src.shared.exceptions.bad_exception import BadRequestException
from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.forbidden_exception import ForbiddenException

class CreateNumberLuckyService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, uuid: str) -> NumberLuckyModelPayload:
        user = self._db.query(User).filter(User.uuid == uuid).first()

        if not user:
            raise NotFoundException(message='Usuário não encontrado')

        if user.is_active == False:
            raise ForbiddenException(message='User is not active')

        lucky_number = str(randrange(100_000_000_000, 999_999_999_999))
        lucky_user_uuid = user.uuid
        lucky_is_active = True

        model = CreateNumberLuckyModel(
            number=lucky_number, 
            user_uuid=lucky_user_uuid, 
            is_active=lucky_is_active
        )

        check_number = self._db.query(NumberLucky).filter(NumberLucky.number == model.number).first()

        if check_number:
            raise BadRequestException('Numero já cadastrado no sistema')

        number_lucky = NumberLucky(**model.dict())
        number_lucky.uuid = str(uuid4())

        self._db.add(number_lucky)
        self._db.commit()
        self._db.refresh(number_lucky)

        number_lucky.user = user

        return NumberLuckyModelPayload.from_orm(number_lucky)

