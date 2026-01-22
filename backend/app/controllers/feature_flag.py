from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.feature_flag import FeatureFlag
from app.schemas.feature_flag import FeatureFlagCreate, FeatureFlagUpdate


def _require_updated_by(payload: FeatureFlagUpdate):
    if payload.updated_by is None:
        raise ValueError("updated_by e obrigatorio em atualizacoes")


async def create_feature_flag(
    db: AsyncSession, payload: FeatureFlagCreate
) -> FeatureFlag:
    feature_flag = FeatureFlag(**payload.dict())
    db.add(feature_flag)
    await db.commit()
    await db.refresh(feature_flag)
    return feature_flag


async def get_feature_flag(db: AsyncSession, feature_flag_id: int) -> FeatureFlag | None:
    result = await db.execute(select(FeatureFlag).where(FeatureFlag.id == feature_flag_id))
    return result.scalar_one_or_none()


async def list_feature_flags(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[FeatureFlag]:
    result = await db.execute(select(FeatureFlag).offset(skip).limit(limit))
    return list(result.scalars().all())


async def update_feature_flag(
    db: AsyncSession, feature_flag: FeatureFlag, payload: FeatureFlagUpdate
) -> FeatureFlag:
    _require_updated_by(payload)
    data = payload.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(feature_flag, key, value)
    await db.commit()
    await db.refresh(feature_flag)
    return feature_flag


async def delete_feature_flag(db: AsyncSession, feature_flag: FeatureFlag) -> None:
    await db.delete(feature_flag)
    await db.commit()
