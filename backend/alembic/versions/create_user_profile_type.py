"""create user_profile_type table

Revision ID: create_user_profile_type
Revises: add_cellphone_birthdate
Create Date: 2025-01-21 00:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "create_user_profile_type"
down_revision = "add_cellphone_birthdate"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user_profile_type",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "profile_type_id",
            sa.Integer(),
            sa.ForeignKey("profile_type.id", ondelete="CASCADE"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("user_profile_type")
