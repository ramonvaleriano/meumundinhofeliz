from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.feature_flag import (
    create_feature_flag,
    delete_feature_flag,
    get_feature_flag,
    list_feature_flags,
    update_feature_flag,
)
from app.core.database import get_db
from app.schemas.feature_flag import FeatureFlagCreate, FeatureFlagRead, FeatureFlagUpdate

router = APIRouter(prefix="/feature-flags", tags=["Feature Flag"])


@router.post("/", response_model=FeatureFlagRead, status_code=status.HTTP_201_CREATED)
async def create(payload: FeatureFlagCreate, db: AsyncSession = Depends(get_db)):
    return await create_feature_flag(db, payload)


@router.get("/{feature_flag_id}", response_model=FeatureFlagRead)
async def read(feature_flag_id: int, db: AsyncSession = Depends(get_db)):
    feature_flag = await get_feature_flag(db, feature_flag_id)
    if not feature_flag:
        raise HTTPException(status_code=404, detail="Feature flag nao encontrada")
    return feature_flag


@router.get("/", response_model=list[FeatureFlagRead])
async def list_all(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await list_feature_flags(db, skip=skip, limit=limit)


@router.put("/{feature_flag_id}", response_model=FeatureFlagRead)
async def update(
    feature_flag_id: int, payload: FeatureFlagUpdate, db: AsyncSession = Depends(get_db)
):
    feature_flag = await get_feature_flag(db, feature_flag_id)
    if not feature_flag:
        raise HTTPException(status_code=404, detail="Feature flag nao encontrada")
    try:
        return await update_feature_flag(db, feature_flag, payload)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{feature_flag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(feature_flag_id: int, db: AsyncSession = Depends(get_db)):
    feature_flag = await get_feature_flag(db, feature_flag_id)
    if not feature_flag:
        raise HTTPException(status_code=404, detail="Feature flag nao encontrada")
    await delete_feature_flag(db, feature_flag)
    return None
