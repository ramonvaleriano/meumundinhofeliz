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

    def create_token(self, cpf: str, email: str) -> str:
        payload = {"cpf": cpf, "email": email}
        data = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode()
        token = self._fernet.encrypt(data)
        return token.hex()

    def validate_token(self, token_hex: str) -> tuple[bool, dict]:
        try:
            token = bytes.fromhex(token_hex)
            ttl = settings.token_exp_minutes * 60
            data = self._fernet.decrypt(token, ttl=ttl)
            return True, json.loads(data.decode())
        except (InvalidToken, ValueError):
            return False, {"cpf": None, "email": None}

    def verify_token_for_cpf(self, token_hex: str, cpf: str) -> tuple[bool, dict]:
        is_valid, data = self.validate_token(token_hex)
        if not is_valid:
            return False, {"message": "token expirado", "cpf": None, "email": None}
        if data.get("cpf") != cpf:
            return False, {
                "message": "usuario nao e compativel ao cpf",
                "cpf": data.get("cpf"),
                "email": data.get("email"),
            }
        return True, data
