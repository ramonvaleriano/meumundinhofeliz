from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.services.crypto_service import PasswordCipher
from app.services.user_identity_service import UserIdentityCipher


def _invalid_credentials() -> ValueError:
    return ValueError("Credenciais invalidas")


def _expired_token() -> ValueError:
    return ValueError("token expirado")


def _invalid_uuid() -> ValueError:
    return ValueError("uuid nao confere com usuario")


async def login(db: AsyncSession, email: str, password: str) -> str:
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        raise ValueError("Usuario nao encontrado")

    password_cipher = PasswordCipher()
    try:
        plain = password_cipher.decrypt(user.password)
    except ValueError as exc:
        raise _invalid_credentials() from exc

    if plain != password:
        raise _invalid_credentials()

    identity = UserIdentityCipher()
    token = identity.create_token(user.cpf, user.email)
    user.token = token
    await db.commit()
    await db.refresh(user)
    return token


async def refresh_token(db: AsyncSession, uuid: str, token: str) -> str:
    identity = UserIdentityCipher()
    is_valid, data = identity.validate_token(token)
    if not is_valid:
        raise _expired_token()

    cpf = data.get("cpf")
    if not cpf:
        raise _expired_token()

    result = await db.execute(select(User).where(User.cpf == cpf))
    user = result.scalar_one_or_none()
    if not user:
        raise ValueError("Usuario nao encontrado")

    if user.uuid != uuid:
        raise _invalid_uuid()

    ok, data_check = identity.verify_token_for_cpf(token, cpf)
    if not ok:
        raise ValueError(data_check.get("message", "token invalido"))

    new_token = identity.create_token(user.cpf, user.email)
    user.token = new_token
    await db.commit()
    await db.refresh(user)
    return new_token
