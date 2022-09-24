"""create two factor table

Revision ID: 8ec000d80678
Revises: ace477d17e28
Create Date: 2022-09-22 19:22:03.366308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec000d80678'
down_revision = 'ace477d17e28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'two_factor',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('user_uuid', sa.String(36), nullable=False),
        sa.Column('code', sa.String(6), nullable=False),
        sa.Column('token', sa.String(50), nullable=False),
        sa.Column('two_factor_type', sa.String(15), nullable=False),
        sa.Column('expires_hours', sa.Integer, nullable=False),
        sa.Column('expires_at', sa.DateTime, nullable=False),
        sa.Column('validated_at', sa.DateTime, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade() -> None:
    pass
