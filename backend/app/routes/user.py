from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.user import (
    create_user,
    delete_user,
    get_user,
    list_users,
    update_user,
)
from app.core.database import get_db
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Usuarios"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, payload)


@router.get("/{user_id}", response_model=UserRead)
async def read(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    return user


@router.get("/", response_model=list[UserRead])
async def list_all(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await list_users(db, skip=skip, limit=limit)


@router.put("/{user_id}", response_model=UserRead)
async def update(user_id: int, payload: UserUpdate, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    try:
        return await update_user(db, user, payload)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{user_id}", response_model=UserRead)
async def partial_update(
    user_id: int, payload: UserUpdate, db: AsyncSession = Depends(get_db)
):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    try:
        return await update_user(db, user, payload)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    await delete_user(db, user)
    return None
