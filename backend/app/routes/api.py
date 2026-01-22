from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.routes.address import router as address_router
from app.routes.feature_flag import router as feature_flag_router
from app.routes.profile_type import router as profile_type_router

router = APIRouter()
router.include_router(address_router)
router.include_router(feature_flag_router)
router.include_router(profile_type_router)


@router.get(
    "/health",
    tags=["Sistema"],
    summary="Healthcheck da API",
    description="Verifica se a API esta ativa e respondendo.",
)
def healthcheck():
    return {"status": "ok"}


@router.get(
    "/db/health",
    tags=["Sistema"],
    summary="Healthcheck do banco de dados",
    description="Verifica se o banco de dados esta acessivel.",
)
async def db_healthcheck(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "up"}

@router.get("/")
def root():
    return {"status": "ok", "message": "API online"}
