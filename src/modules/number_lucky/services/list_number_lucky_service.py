from typing import List
from sqlalchemy.orm import Session

from src.modules.number_lucky.entities.number_lucky import NumberLucky
from src.modules.number_lucky.models import NumberLuckyModelPayload


class ListNumberLuckyService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, filter: bool) -> List[NumberLuckyModelPayload]:

        if filter:
            all_numbers = self._db.query(NumberLucky).filter(NumberLucky.is_active == filter).all()

        all_numbers = self._db.query(NumberLucky).all()

        return [NumberLuckyModelPayload.from_orm(number) for number in all_numbers]