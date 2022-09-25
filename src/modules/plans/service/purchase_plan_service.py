from sqlalchemy.orm import Session

from src.modules.users.entities.user import User

from src.modules.plans.entities.plans import Plans

from src.shared.exceptions.bad_exception import BadRequestException

from src.modules.number_lucky.services.create_number_lucky_service import CreateNumberLuckyService


class PurchasePlanService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, uuid: str, document: str) -> bool:
        user = self._db.query(User).filter(User.document == document).first()

        if not user:
            raise BadRequestException(message="User not found")

        plan = self._db.query(Plans).filter(Plans.uuid == uuid).first()

        if not plan:
            raise BadRequestException(message='Plan not found')
        
        i = 0
        while plan.quantity > i:
            service = CreateNumberLuckyService(self._db)

            service.execute(user.uuid)
            print(i)
            i += 1

        return True