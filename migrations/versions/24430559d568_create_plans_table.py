"""create plans table

Revision ID: 24430559d568
Revises: 5d606834c1f9
Create Date: 2022-09-24 16:22:31.392743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24430559d568'
down_revision = '5d606834c1f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'plans',
        sa.Column('uuid', sa.String(36), nullable=False, unique=True, primary_key=True),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('plans')
