"""add column maximum usage in user table

Revision ID: 23d549ead3ad
Revises: 24430559d568
Create Date: 2022-09-25 14:06:02.371691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23d549ead3ad'
down_revision = '24430559d568'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('max_use', sa.Integer(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('max_use', sa.Integer(), nullable=True))
