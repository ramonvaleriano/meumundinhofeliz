# Services e Utils

Este documento descreve os servicos e utilitarios usados pelo backend.

## Services
### PasswordCipher
Arquivo: `backend/app/services/crypto_service.py`
- Criptografa e descriptografa senhas com Fernet
- Usa `CRYPTO_KEY` do `.env` e converte via `derive_fernet_key`

Metodos:
- `encrypt(password: str) -> str`
- `decrypt(token: str) -> str`

### UserIdentityCipher
Arquivo: `backend/app/services/user_identity_service.py`
- Gera identificadores reversiveis (uuid)
- Gera tokens temporarios e valida expiracao

Metodos principais:
- `create_hash(name, cpf, email)`
- `decode_hash(token_hex)`
- `create_token(cpf, email)`
- `validate_token(token_hex)`
- `verify_token_for_cpf(token_hex, cpf)`

## Utils
### derive_fernet_key
Arquivo: `backend/app/utils/key_utils.py`
- Converte uma string comum em uma chave Fernet valida
- Usa SHA-256 e base64 urlsafe

Isso permite usar chaves simples no `.env`.
