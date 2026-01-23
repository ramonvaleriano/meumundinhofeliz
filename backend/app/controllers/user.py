from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.feature_flag import FeatureFlag
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.crypto_service import PasswordCipher
from app.services.user_identity_service import UserIdentityCipher


def _require_updated_by(payload: UserUpdate) -> None:
    if payload.updated_by is None:
        raise ValueError("updated_by e obrigatorio em atualizacoes")


async def _default_role(db: AsyncSession) -> list[int]:
    result = await db.execute(
        select(FeatureFlag).where(FeatureFlag.name_flag == "average_user")
    )
    feature = result.scalar_one_or_none()
    if feature:
        return [feature.id]
    return []


async def create_user(db: AsyncSession, payload: UserCreate) -> User:
    identity = UserIdentityCipher()
    password_cipher = PasswordCipher()

    uuid = identity.create_hash(payload.name, payload.cpf, payload.email)
    token = identity.create_token(payload.cpf, payload.email)
    password = password_cipher.encrypt(payload.password)

    role = payload.role
    if role is None:
        role = await _default_role(db)

    user = User(
        name=payload.name,
        surname=payload.surname,
        uuid=uuid,
        token=token,
        email=payload.email,
        cpf=payload.cpf,
        password=password,
        address=payload.address,
        is_active=payload.is_active,
        is_verified=payload.is_verified,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
        last_login=payload.last_login,
        role=role,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(db: AsyncSession, user_id: int) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def list_users(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return list(result.scalars().all())


async def update_user(db: AsyncSession, user: User, payload: UserUpdate) -> User:
    _require_updated_by(payload)
    data = payload.model_dump(exclude_unset=True)

    if "password" in data and data["password"] is not None:
        password_cipher = PasswordCipher()
        data["password"] = password_cipher.encrypt(data["password"])

    for key, value in data.items():
        setattr(user, key, value)

    await db.commit()
    await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user: User) -> None:
    await db.delete(user)
    await db.commit()
