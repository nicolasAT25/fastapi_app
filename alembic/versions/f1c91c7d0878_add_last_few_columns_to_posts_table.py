"""Add last few columns to posts table

Revision ID: f1c91c7d0878
Revises: 028eb27b074e
Create Date: 2024-10-20 11:08:05.448373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1c91c7d0878'
down_revision: Union[str, None] = '028eb27b074e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("published", sa.Boolean, nullable=False, server_default="TRUE"),
                  )
    op.add_column("posts",
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
