"""Add date default value

Revision ID: 608643812465
Revises: fc8f1b6da48e
Create Date: 2024-11-25 15:57:50.111018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '608643812465'
down_revision: Union[str, None] = 'fc8f1b6da48e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add a server default to the created_at column
    op.alter_column('users', 'created_at',
        server_default=sa.text('NOW()'),  # Set default to current timestamp
        existing_type=sa.TIMESTAMP,
        existing_nullable=True  # Keep column nullable if it was before
    )


def downgrade() -> None:
    # Remove the server default from created_at
    op.alter_column('users', 'created_at',
        server_default=None,  # Remove the default
        existing_type=sa.TIMESTAMP,
        existing_nullable=True
    )
