"""seed users admin

Revision ID: seed_users
Revises: create_users
Create Date: 2025-01-21 00:00:00
"""

import logging

from alembic import op
import sqlalchemy as sa

from app.core.config import settings
from app.services.crypto_service import PasswordCipher
from app.services.user_identity_service import UserIdentityCipher

# revision identifiers, used by Alembic.
revision = "seed_users"
down_revision = "create_users"
branch_labels = None
depends_on = None

logger = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(sa.text("SELECT COUNT(1) FROM users"))
    count = result.scalar() or 0
    logger.info("seed_users: total atual na tabela users = %s", count)
    if count:
        logger.info("seed_users: tabela users nao esta vazia, seed ignorado")
        return

    try:
        identity = UserIdentityCipher()
        password_cipher = PasswordCipher()
    except Exception as exc:
        logger.exception("seed_users: erro ao inicializar services: %s", exc)
        raise

    name = settings.admin_name
    surname = settings.admin_surname
    email = settings.admin_email
    cpf = settings.admin_cpf
    short_password = settings.admin_password

    if not all([name, surname, email, cpf, short_password]):
        logger.error("seed_users: dados do admin ausentes no .env")
        raise ValueError("Dados do admin ausentes no .env")

    try:
        uuid = identity.create_hash(name, cpf, email)
        token = identity.create_token(cpf, email)
        password = password_cipher.encrypt(short_password)
    except Exception as exc:
        logger.exception("seed_users: erro ao gerar uuid/token/password: %s", exc)
        raise

    users_table = sa.table(
        "users",
        sa.column("name", sa.Text),
        sa.column("surname", sa.Text),
        sa.column("uuid", sa.Text),
        sa.column("token", sa.Text),
        sa.column("email", sa.Text),
        sa.column("cpf", sa.Text),
        sa.column("cellphone", sa.Text),
        sa.column("birth_date", sa.Text),
        sa.column("password", sa.Text),
        sa.column("address", sa.Integer),
        sa.column("is_active", sa.Boolean),
        sa.column("is_verified", sa.Boolean),
        sa.column("created_by", sa.Integer),
        sa.column("updated_by", sa.Integer),
        sa.column("last_login", sa.DateTime),
        sa.column("role", sa.ARRAY(sa.Integer)),
    )

    op.bulk_insert(
        users_table,
        [
            {
                "name": name,
                "surname": surname,
                "uuid": uuid,
                "token": token,
                "email": email,
                "cpf": cpf,
                "cellphone": "00000000000",
                "birth_date": "1900-01-01",
                "password": password,
                "address": None,
                "is_active": True,
                "is_verified": True,
                "created_by": None,
                "updated_by": None,
                "last_login": None,
                "role": [1, 2],
            }
        ],
    )
    logger.info("seed_users: usuario admin inserido com sucesso")


def downgrade() -> None:
    op.execute("DELETE FROM users")
