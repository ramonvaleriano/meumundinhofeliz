import base64
import hashlib


def derive_fernet_key(raw_key: str) -> str:
    if not raw_key:
        raise ValueError("USER_HASH_KEY nao definido")
    digest = hashlib.sha256(raw_key.encode()).digest()
    return base64.urlsafe_b64encode(digest).decode()
