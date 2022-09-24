import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.modules.guests.entities.guest import Guest

from src.config.database import Base

class User(Base):

    __tablename__ = 'users'

    uuid = sa.Column(sa.String, unique=True, primary_key=True, index=True)
    name = sa.Column(sa.String, unique=True, nullable=False)
    document = sa.Column(sa.String, unique=True, nullable=False)
    email = sa.Column(sa.String, nullable=True)
    verified_email = sa.Column(sa.String, nullable=True)
    phone = sa.Column(sa.String, unique=True, nullable=True)
    verified_phone = sa.Column(sa.String, nullable=True)
    is_active = sa.Column(sa.Boolean, default=False)
    # relations
    number_lucky = relationship("NumberLucky", back_populates='user')
    guests = relationship("Guest", back_populates='user')
    # timestamp
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())