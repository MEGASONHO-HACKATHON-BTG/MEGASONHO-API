from sqlalchemy.orm import Session

from src.modules.plans.entities.plans import Plans

from src.shared.exceptions.bad_exception import BadRequestException


class PurchasePlanService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, uuid: str):
        plan = self._db.query(Plans).filter(Plans.uuid == uuid).first()

        if not plan:
            raise BadRequestException(message='Plan not found')

        return