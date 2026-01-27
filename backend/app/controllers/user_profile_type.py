from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.profile_type import ProfileType
from app.models.user import User
from app.models.user_profile_type import UserProfileType
from app.schemas.user_profile_type import UserProfileTypeCreate, UserProfileTypeUpdate


def _require_updated_by(payload: UserProfileTypeUpdate) -> None:
    pass


async def _validate_fk(db: AsyncSession, user_id: int, profile_type_id: int) -> None:
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one_or_none()
    if not user:
        raise ValueError("Usuario nao encontrado")

    profile_result = await db.execute(
        select(ProfileType).where(ProfileType.id == profile_type_id)
    )
    profile = profile_result.scalar_one_or_none()
    if not profile:
        raise ValueError("ProfileType nao encontrado")


async def create_user_profile_type(
    db: AsyncSession, payload: UserProfileTypeCreate
) -> UserProfileType:
    await _validate_fk(db, payload.user_id, payload.profile_type_id)
    relation = UserProfileType(**payload.model_dump())
    db.add(relation)
    await db.commit()
    await db.refresh(relation)
    return relation


async def get_user_profile_type(db: AsyncSession, relation_id: int) -> UserProfileType | None:
    result = await db.execute(
        select(UserProfileType).where(UserProfileType.id == relation_id)
    )
    return result.scalar_one_or_none()


async def list_user_profile_types(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[UserProfileType]:
    result = await db.execute(select(UserProfileType).offset(skip).limit(limit))
    return list(result.scalars().all())


async def update_user_profile_type(
    db: AsyncSession, relation: UserProfileType, payload: UserProfileTypeUpdate
) -> UserProfileType:
    data = payload.model_dump(exclude_unset=True)
    if "user_id" in data or "profile_type_id" in data:
        user_id = data.get("user_id", relation.user_id)
        profile_type_id = data.get("profile_type_id", relation.profile_type_id)
        await _validate_fk(db, user_id, profile_type_id)

    for key, value in data.items():
        setattr(relation, key, value)

    await db.commit()
    await db.refresh(relation)
    return relation


async def delete_user_profile_type(db: AsyncSession, relation: UserProfileType) -> None:
    await db.delete(relation)
    await db.commit()
