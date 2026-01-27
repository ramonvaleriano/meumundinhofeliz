# Tabela UserProfileType

Este documento descreve a tabela de associacao entre `users` e `profile_type`.

## Objetivo
Permitir associar um usuario a um ou mais tipos de perfil (ex: medico, professor, responsavel).

## Estrutura da tabela
Tabela: `user_profile_type`

Colunas:
- `id` (integer, PK, auto incremental)
- `user_id` (integer, FK -> `users.id`, obrigatorio)
- `profile_type_id` (integer, FK -> `profile_type.id`, obrigatorio)

Regras:
- As chaves estrangeiras usam `ON DELETE CASCADE`, entao apagar um usuario remove os relacionamentos automaticamente.

## Schemas da API
Arquivos:
- `backend/app/schemas/user_profile_type.py`

Schemas:
- `UserProfileTypeCreate`: payload de criacao
- `UserProfileTypeUpdate`: payload de atualizacao parcial
- `UserProfileTypeRead`: resposta padrao

Exemplo de payload de criacao:
```json
{
  "user_id": 1,
  "profile_type_id": 2
}
```

## Regras de validacao
- `user_id` precisa existir
- `profile_type_id` precisa existir

## Rotas da API
Base URL: `/api/user-profile-types`
Arquivo das rotas: `backend/app/routes/user_profile_type.py`

### 1) POST /api/user-profile-types/
Cria um relacionamento usuario x profile_type.

Response:
- 201 com `UserProfileTypeRead`

### 2) GET /api/user-profile-types/
Lista todos os relacionamentos.

Query params:
- `skip` (default 0)
- `limit` (default 100)

### 3) GET /api/user-profile-types/{relation_id}
Busca relacionamento por ID.

Response:
- 200 com `UserProfileTypeRead`
- 404 se nao encontrado

### 4) PUT /api/user-profile-types/{relation_id}
Atualiza relacionamento.

Request body:
- `UserProfileTypeUpdate`

Response:
- 200 com `UserProfileTypeRead`
- 404 se relacionamento, usuario ou profile_type nao existirem

### 5) DELETE /api/user-profile-types/{relation_id}
Remove relacionamento.

Response:
- 204 sem conteudo
- 404 se nao encontrado

## Erros comuns
- 404: Usuario nao encontrado
- 404: ProfileType nao encontrado
- 404: Relacionamento nao encontrado
