import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.config.database import Base


class NumberLucky(Base):

    __tablename__ = 'number_lucky'

    uuid = sa.Column(sa.String, nullable=False, primary_key=True, index=True)
    number = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    # relations
    user_uuid = sa.Column(sa.String, sa.ForeignKey('users.uuid'))
    user = relationship("User", back_populates='number_lucky')
    # timestamp
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
