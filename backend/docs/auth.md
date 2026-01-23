# Autenticacao (Auth)

Este documento descreve as rotas de autenticacao da API, como elas funcionam e quais regras de negocio estao envolvidas.

## Objetivo
Permitir login com email e senha, e atualizar (refresh) o token do usuario com base em um token temporario e um UUID.

## Dependencias
- `PasswordCipher` (criptografia de senha)
- `UserIdentityCipher` (geracao e validacao de token)

Arquivos principais:
- `backend/app/routes/auth.py`
- `backend/app/controllers/auth.py`
- `backend/app/schemas/auth.py`

## Rotas
Base URL: `/api/auth`

### 1) POST /api/auth/login
Faz login com email e senha.

Request body:
```json
{
  "email": "ana@email.com",
  "password": "Senha@123"
}
```

Fluxo:
1) Verifica se o email existe.
2) Descriptografa a senha armazenada.
3) Compara com a senha enviada.
4) Gera um novo token, salva no usuario e atualiza `last_login`.

Response (200):
```json
{
  "token": "..."
}
```

Erros possiveis:
- 404: Usuario nao encontrado
- 401: Credenciais invalidas
- 400: Erro inesperado

### 2) POST /api/auth/refresh
Atualiza o token do usuario.

Query params:
- `uuid` (obrigatorio)
- `token` (obrigatorio)

Exemplo:
```
POST /api/auth/refresh?uuid=SEU_UUID&token=SEU_TOKEN
```

Fluxo:
1) Valida se o token ainda e valido (tempo de expiracao).
2) Recupera o `cpf` do token descriptografado.
3) Busca o usuario pelo `cpf`.
4) Verifica se o `uuid` informado confere com o usuario.
5) Gera um novo token, atualiza no usuario e grava `last_login`.

Response (200):
```json
{
  "token": "..."
}
```

Erros possiveis:
- 404: Usuario nao encontrado
- 401: token expirado
- 401: uuid nao confere com usuario
- 400: Erro inesperado

## Regras importantes
- O token tem tempo de expiracao configurado em `TOKEN_EXP_MINUTES` no `.env`.
- O login sempre gera um novo token.
- O refresh so funciona se o token for valido e o UUID corresponder ao usuario correto.
