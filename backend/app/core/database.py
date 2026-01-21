from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.core.config import settings

engine = create_async_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = async_sessionmaker(
    bind=engine, autoflush=False, autocommit=False, class_=AsyncSession
)
Base = declarative_base()


def ensure_database_exists():
    # Create the database if it does not exist yet.
    url = settings.database_url_sync
    if "://" not in url:
        return

    driver_and_user, rest = url.split("://", 1)
    if "/" not in rest:
        return

    base_part, db_name = rest.rsplit("/", 1)
    if not db_name:
        return

    admin_url = f"{driver_and_user}://{base_part}/postgres"
    admin_engine = create_engine(admin_url, isolation_level="AUTOCOMMIT", pool_pre_ping=True)
    try:
        with admin_engine.connect() as connection:
            exists = connection.execute(
                text("SELECT 1 FROM pg_database WHERE datname = :name"),
                {"name": db_name},
            ).scalar()
            if not exists:
                connection.execute(text(f'CREATE DATABASE "{db_name}"'))
    finally:
        admin_engine.dispose()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
