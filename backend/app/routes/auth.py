from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.auth import login, refresh_token
from app.core.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Autenticacao"])


@router.post("/login", response_model=TokenResponse)
async def login_route(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    try:
        token = await login(db, payload.email, payload.password)
        return {"token": token}
    except ValueError as exc:
        if str(exc) == "Usuario nao encontrado":
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        if str(exc) == "Credenciais invalidas":
            raise HTTPException(status_code=401, detail=str(exc)) from exc
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/refresh", response_model=TokenResponse)
async def refresh_route(
    uuid: str = Query(..., description="UUID do usuario"),
    token: str = Query(..., description="Token atual do usuario"),
    db: AsyncSession = Depends(get_db),
):
    try:
        new_token = await refresh_token(db, uuid, token)
        return {"token": new_token}
    except ValueError as exc:
        msg = str(exc)
        if msg == "Usuario nao encontrado":
            raise HTTPException(status_code=404, detail=msg) from exc
        if msg in ("token expirado", "token invalido", "uuid nao confere com usuario"):
            raise HTTPException(status_code=401, detail=msg) from exc
        raise HTTPException(status_code=400, detail=msg) from exc
