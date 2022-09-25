"""add column code in user table

Revision ID: 19aebe0e9cca
Revises: 23d549ead3ad
Create Date: 2022-09-25 14:37:14.459888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19aebe0e9cca'
down_revision = '23d549ead3ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code', sa.String(50), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code', sa.String(50), nullable=True))
