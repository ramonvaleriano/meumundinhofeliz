"""create profile_type table

Revision ID: create_profile_type
Revises: 0001_create_address
Create Date: 2025-01-21 00:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "create_profile_type"
down_revision = "0001_create_address"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "profile_type",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_type", sa.String(length=100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("profile_type")
