from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.profile_type import ProfileType
from app.schemas.profile_type import ProfileTypeCreate, ProfileTypeUpdate


async def create_profile_type(
    db: AsyncSession, payload: ProfileTypeCreate
) -> ProfileType:
    profile_type = ProfileType(**payload.dict())
    db.add(profile_type)
    await db.commit()
    await db.refresh(profile_type)
    return profile_type


async def get_profile_type(
    db: AsyncSession, profile_type_id: int
) -> ProfileType | None:
    result = await db.execute(
        select(ProfileType).where(ProfileType.id == profile_type_id)
    )
    return result.scalar_one_or_none()


async def list_profile_types(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[ProfileType]:
    result = await db.execute(select(ProfileType).offset(skip).limit(limit))
    return list(result.scalars().all())


async def update_profile_type(
    db: AsyncSession, profile_type: ProfileType, payload: ProfileTypeUpdate
) -> ProfileType:
    data = payload.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(profile_type, key, value)
    await db.commit()
    await db.refresh(profile_type)
    return profile_type


async def delete_profile_type(db: AsyncSession, profile_type: ProfileType) -> None:
    await db.delete(profile_type)
    await db.commit()
