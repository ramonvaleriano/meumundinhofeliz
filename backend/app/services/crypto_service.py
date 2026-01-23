from cryptography.fernet import Fernet, InvalidToken

from app.core.config import settings
from app.utils.key_utils import derive_fernet_key

class PasswordCipher:
    def __init__(self, key: str | None = None):
        raw_key = key or settings.crypto_key
        fernet_key = derive_fernet_key(raw_key)
        self._fernet = Fernet(fernet_key.encode())

    def encrypt(self, password: str) -> str:
        token = self._fernet.encrypt(password.encode())
        return token.decode()

    def decrypt(self, token: str) -> str:
        try:
            data = self._fernet.decrypt(token.encode())
            return data.decode()
        except InvalidToken as exc:
            raise ValueError("Token invalido ou chave incorreta") from exc
