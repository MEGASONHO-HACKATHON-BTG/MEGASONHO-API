import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.config.database import Base


class Guest(Base):
    
    __tablename__ = 'guests'

    uuid = sa.Column(sa.String, nullable=False, primary_key=True, index=True)
    name = sa.Column(sa.String, nullable=False)
    phone = sa.Column(sa.String, nullable=True)
    # relations
    user_uuid = sa.Column(sa.String, sa.ForeignKey('users.uuid'))
    user = relationship("User", back_populates='guests')
    # timestamp
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
