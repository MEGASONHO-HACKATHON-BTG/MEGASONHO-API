from datetime import datetime
from sqlalchemy.orm import Session

from src.modules.two_factor.models import TwoFactorModel, ActivateTwoFactorModel
from src.modules.two_factor.entities.two_factor import TwoFactor

from src.modules.users.entities.user import User

from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.forbidden_exception import ForbiddenException
from src.shared.exceptions.bad_exception import BadRequestException


class ActivateTwoFactorService:

    def __init__(self, db: Session):
        self._db = db

    def execute(self, model: ActivateTwoFactorModel) -> TwoFactorModel:
        two_factor = self._db.query(TwoFactor).filter(TwoFactor.token == model.token).first()

        if not two_factor:
            raise NotFoundException(message='Token de ativação não encontrado')

        if two_factor.expires_at < datetime.now():
            raise ForbiddenException(message='Token de ativação vencido')

        if two_factor.validated_at:
            raise BadRequestException(message='Token de ativação já esta ativado')

        if two_factor.code != model.code:
            raise ForbiddenException(message='Código incorreto')
        
        two_factor.validated_at = datetime.now()

        user = self._db.query(User).filter(User.uuid == two_factor.user_uuid).first()

        if not user:
            raise BadRequestException(message='Usuário não encontrado')
        
        if two_factor.two_factor_type == 'WHATSAPP':
            user.verified_phone = True
            user.is_active = True

            self._db.add(user)
            self._db.commit()
            self._db.refresh(user)

        self._db.add(two_factor)
        self._db.commit()
        self._db.refresh(two_factor)

        if not two_factor:
            raise BadRequestException(message='Erro ao ativar two factor')
        
        return TwoFactorModel.from_orm(two_factor)