import sqlalchemy as sa

from src.config.database import Base

class TwoFactor(Base):

    __tablename__ = 'two_factor'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    user_uuid = sa.Column(sa.String, nullable=False)
    code = sa.Column(sa.String, nullable=False)
    token = sa.Column(sa.String, nullable=False)
    two_factor_type = sa.Column(sa.String, default='whatsapp')
    expires_hours = sa.Column(sa.Integer, nullable=True, default=2)
    expires_at = sa.Column(sa.DateTime, nullable=False)
    validated_at = sa.Column(sa.DateTime, nullable=True)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())