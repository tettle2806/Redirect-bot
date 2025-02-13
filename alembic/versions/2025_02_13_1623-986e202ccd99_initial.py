"""initial

Revision ID: 986e202ccd99
Revises:
Create Date: 2025-02-13 16:23:58.777549

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "986e202ccd99"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("telegram_id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "chats",
        sa.Column("telegram_id", sa.Integer(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("chat_name", sa.String(length=32), nullable=False),
        sa.Column("chat_type", sa.String(length=32), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.telegram_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("chat_name"),
    )
    op.create_table(
        "messages",
        sa.Column("sender_id", sa.Integer(), nullable=False),
        sa.Column("recipient_id", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["recipient_id"],
            ["chats.telegram_id"],
        ),
        sa.ForeignKeyConstraint(
            ["sender_id"],
            ["chats.telegram_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "projects",
        sa.Column("project_name", sa.String(length=32), nullable=False),
        sa.Column("sender_id", sa.Integer(), nullable=False),
        sa.Column("recipient_id", sa.Integer(), nullable=False),
        sa.Column("status", sa.Boolean(), nullable=False),
        sa.Column("keyword", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["recipient_id"],
            ["chats.telegram_id"],
        ),
        sa.ForeignKeyConstraint(
            ["sender_id"],
            ["chats.telegram_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("projects")
    op.drop_table("messages")
    op.drop_table("chats")
    op.drop_table("users")
    # ### end Alembic commands ###
