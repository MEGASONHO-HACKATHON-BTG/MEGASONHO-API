import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.config.database import Base


class Plans(Base):
    
    __tablename__ = 'plans'

    uuid = sa.Column(sa.String, nullable=False, primary_key=True, index=True)
    price = sa.Column(sa.Integer, nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    # timestamp
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
