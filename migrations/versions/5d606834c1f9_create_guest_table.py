"""create guest table

Revision ID: 5d606834c1f9
Revises: 887d4c0b0b25
Create Date: 2022-09-24 14:43:48.832785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d606834c1f9'
down_revision = '887d4c0b0b25'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'guests',
        sa.Column('uuid', sa.String(36), nullable=False, unique=True, primary_key=True),
        sa.Column('user_uuid', sa.String(36), sa.ForeignKey('users.uuid'), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('phone', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('guests')
