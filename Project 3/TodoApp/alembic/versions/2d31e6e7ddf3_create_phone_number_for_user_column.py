"""create phone number for user column

Revision ID: 2d31e6e7ddf3
Revises: 
Create Date: 2024-08-28 14:55:48.146258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d31e6e7ddf3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(255),nullable = True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
