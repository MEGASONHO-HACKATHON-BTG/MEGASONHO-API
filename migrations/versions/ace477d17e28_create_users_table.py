"""create users table

Revision ID: ace477d17e28
Revises: 
Create Date: 2022-09-22 13:52:54.878412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ace477d17e28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('uuid', sa.String(36), nullable=False, unique=True, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False, unique=True),
        sa.Column('document', sa.String(20), nullable=False, unique=True),
        sa.Column('email', sa.String(255), nullable=True, unique=True),
        sa.Column('verified_email', sa.Boolean, nullable=True),
        sa.Column('phone', sa.String(20), nullable=True, unique=True),
        sa.Column('verified_phone', sa.Boolean, nullable=True),
        sa.Column('is_active', sa.Boolean, default=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('users')
