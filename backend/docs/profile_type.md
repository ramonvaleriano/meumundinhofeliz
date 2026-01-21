# Tabela ProfileType (Tipo de Perfil)

Este documento descreve a tabela `profile_type`, seu schema, objetivos e todas as rotas do CRUD expostas pela API.

## Objetivo
Armazenar tipos de perfis de usuario (ex: profissionais, pais, especialistas). Essa tabela pode ser usada para classificar usuarios em telas e fluxos da aplicacao.

## Estrutura da tabela
Tabela: `profile_type`

Colunas:
- `id` (integer, PK, auto incremental)
- `user_type` (string, obrigatorio)

Model:
- arquivo: `backend/app/models/profile_type.py`

## Regras de validacao
No momento, as validacoes sao simples:
- `user_type` e obrigatorio
- tipo string

## Schemas da API
Arquivos:
- `backend/app/schemas/profile_type.py`

Schemas:
- `ProfileTypeCreate`: payload de criacao
- `ProfileTypeUpdate`: payload de atualizacao parcial
- `ProfileTypeRead`: resposta padrao

Exemplo de payload de criacao:
```json
{
  "user_type": "Neuropediatra"
}
```

## Regras de persistencia
Controller:
- arquivo: `backend/app/controllers/profile_type.py`

Funcoes:
- `create_profile_type`: cria e salva o tipo de perfil
- `get_profile_type`: busca por ID
- `list_profile_types`: lista com paginacao
- `update_profile_type`: atualiza campos presentes no payload
- `delete_profile_type`: remove o registro

## Rotas da API
Base URL: `/api/profile-types`
Arquivo das rotas: `backend/app/routes/profile_type.py`

### 1) POST /api/profile-types/
Cria um tipo de perfil.

Request body:
- `ProfileTypeCreate`

Response:
- 201 com `ProfileTypeRead`

Exemplo de resposta:
```json
{
  "id": 1,
  "user_type": "Neuropediatra"
}
```

### 2) GET /api/profile-types/
Lista todos os tipos de perfil.

Query params:
- `skip` (default 0)
- `limit` (default 100)

Response:
- 200 com lista de `ProfileTypeRead`

### 3) GET /api/profile-types/{profile_type_id}
Busca um tipo de perfil pelo ID.

Response:
- 200 com `ProfileTypeRead`
- 404 se nao encontrado

### 4) PUT /api/profile-types/{profile_type_id}
Atualiza um tipo de perfil existente.

Request body:
- `ProfileTypeUpdate` (parcial)

Response:
- 200 com `ProfileTypeRead`
- 404 se nao encontrado

### 5) DELETE /api/profile-types/{profile_type_id}
Remove um tipo de perfil.

Response:
- 204 sem conteudo
- 404 se nao encontrado

## Erros comuns
- 404: perfil nao encontrado
- 500: erro inesperado no banco ou na API

## Observacoes finais
- As migrations garantem que a tabela exista antes de usar as rotas.
- Se novas colunas forem adicionadas, e necessario criar migration.
- As rotas aparecem no `/docs` e `/redoc` do FastAPI.
