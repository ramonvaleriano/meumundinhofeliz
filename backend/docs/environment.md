# Variaveis de Ambiente (.env)

Este documento lista todas as variaveis utilizadas pelo backend e seu significado.

## Variaveis obrigatorias
- `DATABASE_URL`: string de conexao async com Postgres (ex: `postgresql+asyncpg://user@host:5432/db`)

## Variaveis recomendadas
- `PROJECT_NAME`: nome exibido na API (Swagger)
- `CRYPTO_KEY`: chave base para criptografia de senhas (pode ser string simples)
- `USER_HASH_KEY`: chave base para identidade e tokens (pode ser string simples)
- `TOKEN_EXP_MINUTES`: tempo de expiracao de token em minutos (default 30)

## Variaveis do usuario admin (seed)
- `ADMIN_NAME`
- `ADMIN_SURNAME`
- `ADMIN_EMAIL`
- `ADMIN_CPF`
- `ADMIN_PASSWORD`

## Observacoes
- `CRYPTO_KEY` e `USER_HASH_KEY` sao transformadas em uma chave Fernet valida pelo `derive_fernet_key`.
- Se alguma variavel do admin estiver ausente, o seed falha e nao cria o usuario.

Exemplo:
```env
PROJECT_NAME="Meu Mundinho Feliz API"
DATABASE_URL="postgresql+asyncpg://postgres@localhost:5432/meumundinho"
CRYPTO_KEY="meumundo"
USER_HASH_KEY="meumundo"
TOKEN_EXP_MINUTES="30"
ADMIN_NAME="Admin"
ADMIN_SURNAME="Admin"
ADMIN_EMAIL="ana.admin@empresa.com.br"
ADMIN_CPF="987.654.321-11"
ADMIN_PASSWORD="meumundinho12345"
```
