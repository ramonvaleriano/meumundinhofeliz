# Servico de Identidade do Usuario (UserIdentityCipher)

Este documento descreve o servico de identificacao criptografada de usuarios, usado para gerar um identificador reversivel com base em `name`, `cpf` e `email`.

## Objetivo
Criar um identificador seguro e reversivel para um usuario, sem depender de tempo (nao expira), permitindo recuperar os dados originais quando necessario.

## Implementacao
Arquivos:
- `backend/app/services/user_identity_service.py`
- `backend/app/utils/key_utils.py`

Classes:
- `UserIdentityCipher`

Biblioteca usada:
- `cryptography` (Fernet)

## Como funciona
1) O servico recebe `name`, `cpf` e `email`.
2) Esses dados sao serializados em JSON de forma compacta.
3) O JSON e criptografado com Fernet usando uma chave derivada de `USER_HASH_KEY`.
4) O resultado e convertido para hexadecimal (string curta e segura para transporte).

O processo e reversivel: ao receber o hash em hex, o servico descriptografa e recupera os dados originais.

## Variaveis de ambiente
No arquivo `.env`:
```
USER_HASH_KEY="meumundo"
```

Observacao: a chave original nao precisa estar no formato Fernet. Ela e convertida automaticamente pelo `derive_fernet_key`.

## Importancia do derive_fernet_key
Arquivo: `backend/app/utils/key_utils.py`

A funcao `derive_fernet_key` transforma uma string simples em uma chave valida para Fernet:
- Faz hash SHA-256 da string (`USER_HASH_KEY`)
- Converte para base64 urlsafe
- O resultado tem 32 bytes, formato exigido pela biblioteca

Isso permite que voce use uma chave simples no `.env` (ex: `meumundo`) sem quebrar o funcionamento do Fernet.

## Metodos
### 1) create_hash(name: str, cpf: str, email: str) -> str
Gera um hash reversivel com base nos dados informados.

Exemplo:
```python
from app.services.user_identity_service import UserIdentityCipher

cipher = UserIdentityCipher()
user_hash = cipher.create_hash("Ana", "123.456.789-00", "ana@email.com")
```

### 2) decode_hash(token_hex: str) -> dict
Reverte o hash e retorna um dicionario com `name`, `cpf` e `email`.

Exemplo:
```python
from app.services.user_identity_service import UserIdentityCipher

cipher = UserIdentityCipher()
original = cipher.decode_hash(user_hash)
```

Exemplo de retorno:
```json
{
  "name": "Ana",
  "cpf": "123.456.789-00",
  "email": "ana@email.com"
}
```

## Erros comuns
- `ValueError: USER_HASH_KEY nao definido`: a variavel nao foi configurada no `.env`.
- `ValueError: Hash invalido ou chave incorreta`: o token foi alterado ou a chave esta errada.

## Observacoes finais
- O hash e criptografado e reversivel (nao e hash irreversivel).
- Use quando precisar reobter os dados originais.
- Nao usar este servico como hash de senha.
