"""add name_flag to feature_flag

Revision ID: add_name_flag_to_feature_flag
Revises: create_feature_flag
Create Date: 2025-01-21 00:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "add_name_flag_to_feature_flag"
down_revision = "create_feature_flag"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("feature_flag", sa.Column("name_flag", sa.Text(), nullable=True))
    op.execute("UPDATE feature_flag SET name_flag = 'flag_padrao' WHERE name_flag IS NULL")
    op.alter_column("feature_flag", "name_flag", nullable=False)


def downgrade() -> None:
    op.drop_column("feature_flag", "name_flag")
