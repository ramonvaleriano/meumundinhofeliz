"""seed feature_flag values

Revision ID: seed_feature_flag
Revises: add_name_flag_to_feature_flag
Create Date: 2025-01-21 00:00:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "seed_feature_flag"
down_revision = "add_name_flag_to_feature_flag"
branch_labels = None
depends_on = None


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(sa.text("SELECT COUNT(1) FROM feature_flag"))
    count = result.scalar() or 0
    if count:
        return

    feature_flag_table = sa.table(
        "feature_flag",
        sa.column("name_flag", sa.Text),
        sa.column("is_enabled", sa.Boolean),
        sa.column("status", sa.Text),
        sa.column("strategy", sa.Text),
        sa.column("variation", sa.Text),
        sa.column("created_by", sa.Integer),
        sa.column("updated_by", sa.Integer),
    )

    values = [
        {
            "name_flag": "average_user",
            "is_enabled": True,
            "status": "active",
            "strategy": "restricted_access",
            "variation": '{"percentage": 25, "target_group": "standard_users"}',
            "created_by": None,
            "updated_by": None,
        },
        {
            "name_flag": "admin_super",
            "is_enabled": True,
            "status": "active",
            "strategy": "unrestricted_access",
            "variation": '{"allowed_roles": ["admin", "superadmin"], "visible_logs": true}',
            "created_by": None,
            "updated_by": None,
        },
        {
            "name_flag": "professional_tools",
            "is_enabled": True,
            "status": "active",
            "strategy": "role_based_access",
            "variation": '{"features": ["advanced_analytics", "bulk_export"], "allowed_roles": ["pro", "specialist"]}',
            "created_by": None,
            "updated_by": None,
        },
    ]

    op.bulk_insert(feature_flag_table, values)


def downgrade() -> None:
    op.execute("DELETE FROM feature_flag")
