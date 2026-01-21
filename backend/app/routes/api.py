from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.routes.address import router as address_router
from app.routes.profile_type import router as profile_type_router

router = APIRouter()
router.include_router(address_router)
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
def db_healthcheck(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "up"}

@router.get("/")
def root():
    return {"status": "ok", "message": "API online"}
