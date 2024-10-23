"""Add content column to posts table

Revision ID: a4a4f160286c
Revises: 9d3273abee7a
Create Date: 2024-10-20 10:20:22.445628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4a4f160286c'
down_revision: Union[str, None] = '9d3273abee7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
