from sqlalchemy.orm import Session

from src.modules.users.entities.user import User

from src.shared.exceptions.bad_exception import BadRequestException


class GetUserByDocumentService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, document: str) -> bool:
        user = self._db.query(User).filter(User.document == document).first()

        if user:
            raise BadRequestException(message='CPF já cadastrado')

        return True