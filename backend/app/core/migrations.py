from pathlib import Path

from alembic import command
from alembic.config import Config

from app.core.config import settings


def run_migrations():
    base_dir = Path(__file__).resolve().parents[2]
    alembic_ini = base_dir / "alembic.ini"
    config = Config(str(alembic_ini))
    config.set_main_option("sqlalchemy.url", settings.database_url)
    command.upgrade(config, "head")
