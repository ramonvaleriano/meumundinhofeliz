import json

from cryptography.fernet import Fernet, InvalidToken

from app.core.config import settings
from app.utils.key_utils import derive_fernet_key


class UserIdentityCipher:
    def __init__(self, key: str | None = None):
        raw_key = key or settings.user_hash_key
        fernet_key = derive_fernet_key(raw_key)
        self._fernet = Fernet(fernet_key.encode())

    def create_hash(self, name: str, cpf: str, email: str) -> str:
        payload = {"name": name, "cpf": cpf, "email": email}
        data = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode()
        token = self._fernet.encrypt(data)
        return token.hex()

    def decode_hash(self, token_hex: str) -> dict:
        try:
            token = bytes.fromhex(token_hex)
            data = self._fernet.decrypt(token)
            return json.loads(data.decode())
        except (InvalidToken, ValueError) as exc:
            raise ValueError("Hash invalido ou chave incorreta") from exc
