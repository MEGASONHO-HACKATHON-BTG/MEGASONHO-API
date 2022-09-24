"""create number lucky table

Revision ID: 887d4c0b0b25
Revises: 8ec000d80678
Create Date: 2022-09-23 10:15:30.543553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '887d4c0b0b25'
down_revision = '8ec000d80678'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'number_lucky',
        sa.Column('uuid', sa.String(36), nullable=False, unique=True, primary_key=True),
        sa.Column('user_uuid', sa.Integer(), sa.ForeignKey('users.uuid'), nullable=False),
        sa.Column('number', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('number_lucky')
