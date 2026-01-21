from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.profile_type import (
    create_profile_type,
    delete_profile_type,
    get_profile_type,
    list_profile_types,
    update_profile_type,
)
from app.core.database import get_db
from app.schemas.profile_type import ProfileTypeCreate, ProfileTypeRead, ProfileTypeUpdate

router = APIRouter(prefix="/profile-types", tags=["Perfil"])


@router.post("/", response_model=ProfileTypeRead, status_code=status.HTTP_201_CREATED)
async def create(payload: ProfileTypeCreate, db: AsyncSession = Depends(get_db)):
    return await create_profile_type(db, payload)


@router.get("/{profile_type_id}", response_model=ProfileTypeRead)
async def read(profile_type_id: int, db: AsyncSession = Depends(get_db)):
    profile_type = await get_profile_type(db, profile_type_id)
    if not profile_type:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado")
    return profile_type


@router.get("/", response_model=list[ProfileTypeRead])
async def list_all(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    return await list_profile_types(db, skip=skip, limit=limit)


@router.put("/{profile_type_id}", response_model=ProfileTypeRead)
async def update(
    profile_type_id: int, payload: ProfileTypeUpdate, db: AsyncSession = Depends(get_db)
):
    profile_type = await get_profile_type(db, profile_type_id)
    if not profile_type:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado")
    return await update_profile_type(db, profile_type, payload)


@router.delete("/{profile_type_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(profile_type_id: int, db: AsyncSession = Depends(get_db)):
    profile_type = await get_profile_type(db, profile_type_id)
    if not profile_type:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado")
    await delete_profile_type(db, profile_type)
    return None
