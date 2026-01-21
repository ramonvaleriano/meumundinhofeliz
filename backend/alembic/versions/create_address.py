"""create address table

Revision ID: 0001_create_address
Revises: 
Create Date: 2025-01-21 00:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0001_create_address"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cep", sa.String(length=20), nullable=False),
        sa.Column("estado", sa.String(length=50), nullable=False),
        sa.Column("bairro", sa.String(length=100), nullable=False),
        sa.Column("tipo_logradouro", sa.String(length=100), nullable=False),
        sa.Column("logradouro", sa.String(length=200), nullable=False),
        sa.Column("numero", sa.String(length=50), nullable=False),
        sa.Column("complemento", sa.String(length=200), nullable=True),
        sa.Column("referencia", sa.String(length=200), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("address")
