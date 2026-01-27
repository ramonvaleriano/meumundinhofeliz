from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.user_profile_type import (
    create_user_profile_type,
    delete_user_profile_type,
    get_user_profile_type,
    list_user_profile_types,
    update_user_profile_type,
)
from app.core.database import get_db
from app.schemas.user_profile_type import (
    UserProfileTypeCreate,
    UserProfileTypeRead,
    UserProfileTypeUpdate,
)

router = APIRouter(prefix="/user-profile-types", tags=["User Profile Type"])


@router.post("/", response_model=UserProfileTypeRead, status_code=status.HTTP_201_CREATED)
async def create(payload: UserProfileTypeCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_user_profile_type(db, payload)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/{relation_id}", response_model=UserProfileTypeRead)
async def read(relation_id: int, db: AsyncSession = Depends(get_db)):
    relation = await get_user_profile_type(db, relation_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relacionamento nao encontrado")
    return relation


@router.get("/", response_model=list[UserProfileTypeRead])
async def list_all(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await list_user_profile_types(db, skip=skip, limit=limit)


@router.put("/{relation_id}", response_model=UserProfileTypeRead)
async def update(
    relation_id: int, payload: UserProfileTypeUpdate, db: AsyncSession = Depends(get_db)
):
    relation = await get_user_profile_type(db, relation_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relacionamento nao encontrado")
    try:
        return await update_user_profile_type(db, relation, payload)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.delete("/{relation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(relation_id: int, db: AsyncSession = Depends(get_db)):
    relation = await get_user_profile_type(db, relation_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relacionamento nao encontrado")
    await delete_user_profile_type(db, relation)
    return None
