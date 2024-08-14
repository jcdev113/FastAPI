"""Create phone number for user column

Revision ID: 3fbbf83d9172
Revises: 
Create Date: 2024-08-02 06:12:25.629105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fbbf83d9172'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', 
                  sa.Column('phone_number', sa.String(45), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
