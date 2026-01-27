# Tabela Users (Usuarios)

Este documento descreve a tabela `users`, suas regras de negocio, o CRUD completo e a integracao com os servicos de criptografia do projeto.

## Objetivo
Armazenar usuarios do sistema, incluindo dados de identificacao, credenciais criptografadas, flags de status e informacoes de auditoria.

## Estrutura da tabela
Tabela: `users`

Colunas:
- `id` (integer, PK, auto incremental)
- `name` (string, obrigatorio)
- `surname` (string, obrigatorio)
- `uuid` (string longa, obrigatorio, gerado automaticamente)
- `token` (string longa, obrigatorio, refresh token gerado automaticamente)
- `email` (string, obrigatorio)
- `cpf` (string, obrigatorio)
- `cellphone` (string, obrigatorio)
- `birth_date` (string, obrigatorio)
- `password` (string, obrigatorio, criptografado)
- `address` (integer, FK para `address.id`, opcional)
- `is_active` (boolean, obrigatorio, default `true`)
- `is_verified` (boolean, opcional)
- `created_at` (datetime, gerado automaticamente)
- `updated_at` (datetime, gerado automaticamente e atualizado em alteracoes)
- `created_by` (integer, opcional)
- `updated_by` (integer, opcional, obrigatorio em update)
- `last_login` (datetime, opcional)
- `role` (array de inteiros, default `[]`)

Model:
- arquivo: `backend/app/models/user.py`

## Regras de negocio
### 1) uuid automatico
O campo `uuid` nao pode ser alterado. Ele e gerado no momento da criacao usando o servico `UserIdentityCipher` com:

```
create_hash(name, cpf, email)
```

### 2) token automatico (refresh token)
O campo `token` e gerado no momento da criacao usando `UserIdentityCipher` com:
```
create_token(cpf, email)
```

### 2) password criptografado
O campo `password` e sempre criptografado com `PasswordCipher` antes de salvar.

### 3) role default
Se `role` nao for enviado no payload, o sistema tenta usar a feature flag `average_user`:
- Se existir, o valor vira `[id_da_feature_flag]`
- Se nao existir, o valor fica `[]`

### 4) updated_by obrigatorio em update
Toda atualizacao exige `updated_by` no payload.

## Integracao com services
### PasswordCipher
Arquivo: `backend/app/services/crypto_service.py`
- Usado para criptografar e descriptografar senhas.
- No CRUD de usuarios, o `password` sempre e criptografado antes de salvar.

### UserIdentityCipher
Arquivo: `backend/app/services/user_identity_service.py`
- Usado para gerar o `uuid` de forma reversivel.
- Cria um identificador a partir de `name`, `cpf` e `email`.

## Schemas da API
Arquivos:
- `backend/app/schemas/user.py`

Schemas:
- `UserCreate`: payload de criacao
- `UserUpdate`: payload de atualizacao (parcial)
- `UserRead`: resposta padrao

Exemplo de payload de criacao:
```json
{
  "name": "Ana",
  "surname": "Silva",
  "email": "ana@email.com",
  "cpf": "123.456.789-00",
  "cellphone": "(11) 99999-9999",
  "birth_date": "2000-01-01",
  "password": "Senha@123",
  "address": 1,
  "is_active": true,
  "is_verified": false,
  "created_by": 10,
  "updated_by": 10,
  "role": [1]
}
```

## Regras de persistencia
Controller:
- arquivo: `backend/app/controllers/user.py`

Funcoes:
- `create_user`: cria usuario e aplica uuid/password/role
- `get_user`: busca por ID
- `list_users`: lista com paginacao
- `update_user`: atualizacao parcial
- `delete_user`: remove o registro

## Rotas da API
Base URL: `/api/users`
Arquivo das rotas: `backend/app/routes/user.py`

### 1) POST /api/users/
Cria um usuario.

Request body:
- `UserCreate`

Response:
- 201 com `UserRead`

### 2) GET /api/users/
Lista todos os usuarios.

Query params:
- `skip` (default 0)
- `limit` (default 100)

Response:
- 200 com lista de `UserRead`

### 3) GET /api/users/{user_id}
Busca um usuario pelo ID.

Response:
- 200 com `UserRead`
- 404 se nao encontrado

### 4) PUT /api/users/{user_id}
Atualiza um usuario.

Request body:
- `UserUpdate` (parcial)
- `updated_by` obrigatorio

Response:
- 200 com `UserRead`
- 404 se nao encontrado
- 422 se `updated_by` nao for informado

### 5) PATCH /api/users/{user_id}
Atualizacao parcial, aceita apenas os campos enviados.

Request body:
- `UserUpdate` (parcial)
- `updated_by` obrigatorio

Response:
- 200 com `UserRead`
- 404 se nao encontrado
- 422 se `updated_by` nao for informado

### 6) DELETE /api/users/{user_id}
Remove um usuario.

Response:
- 204 sem conteudo
- 404 se nao encontrado

## Erros comuns
- 404: usuario nao encontrado
- 422: `updated_by` nao informado em atualizacao
- 500: erro inesperado no banco ou na API

## Observacoes finais
- O `uuid` nao deve ser alterado manualmente.
- O campo `password` salvo no banco e criptografado.
- Para autenticar usuarios, e recomendado usar hash (ex: bcrypt) em vez de criptografia reversivel.

## Dados iniciais (seed automatico)
Existe uma migration que popula automaticamente a tabela quando ela estiver vazia. Isso garante que, em um banco novo, o usuario administrador ja esteja disponivel sem insercao manual.

Usuario admin inserido:
```json
{
  "name": "Admin",
  "surname": "Admin",
  "email": "ana.admin@empresa.com.br",
  "cpf": "987.654.321-11",
  "cellphone": "00000000000",
  "birth_date": "1900-01-01",
  "password": "meumundinho12345",
  "role": [1, 2],
  "is_active": true,
  "is_verified": true
}
```

Observacoes:
- `uuid` e gerado por `UserIdentityCipher.create_hash`.
- `token` e gerado por `UserIdentityCipher.create_token`.
- `password` e criptografado por `PasswordCipher.encrypt`.
