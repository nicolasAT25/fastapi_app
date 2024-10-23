"""Add foreign key to posts table

Revision ID: 028eb27b074e
Revises: 936e09c6c7ff
Create Date: 2024-10-20 10:44:50.288200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '028eb27b074e'
down_revision: Union[str, None] = '936e09c6c7ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_column("posts", "owner_id")
    op.drop_constraint("post_users_fk", table_name="posts")
    pass
