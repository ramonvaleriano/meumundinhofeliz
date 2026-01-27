"""add cellphone and birth_date to users

Revision ID: add_cellphone_birthdate
Revises: seed_users
Create Date: 2025-01-21 00:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "add_cellphone_birthdate"
down_revision = "seed_users"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("cellphone", sa.Text(), nullable=True))
    op.add_column("users", sa.Column("birth_date", sa.Text(), nullable=True))
    op.execute("UPDATE users SET cellphone = '00000000000' WHERE cellphone IS NULL")
    op.execute("UPDATE users SET birth_date = '1900-01-01' WHERE birth_date IS NULL")
    op.alter_column("users", "cellphone", nullable=False)
    op.alter_column("users", "birth_date", nullable=False)


def downgrade() -> None:
    op.drop_column("users", "birth_date")
    op.drop_column("users", "cellphone")
