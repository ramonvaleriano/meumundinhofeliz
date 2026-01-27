# Tabela FeatureFlag

Este documento descreve a tabela `feature_flag`, seu schema, objetivos e todas as rotas do CRUD expostas pela API.

## Objetivo
Controlar funcionalidades liberadas ou bloqueadas na aplicacao, com estrategia e variacoes configuraveis por feature.

## Estrutura da tabela
Tabela: `feature_flag`

Colunas:
- `id` (integer, PK, auto incremental)
- `name_flag` (string longa, obrigatorio)
- `is_enabled` (boolean, obrigatorio, default `true`)
- `status` (string longa, opcional)
- `strategy` (string longa, obrigatorio)
- `variation` (string longa, opcional)
- `created_at` (datetime, gerado automaticamente na criacao)
- `updated_at` (datetime, gerado na criacao e atualizado em toda alteracao)
- `created_by` (integer, opcional)
- `updated_by` (integer, opcional, obrigatorio nas atualizacoes)

Model:
- arquivo: `backend/app/models/feature_flag.py`

## Regras de validacao
- `is_enabled` sempre existe e por padrao e `true`
- `strategy` e obrigatorio
- `updated_by` e obrigatorio em atualizacoes (PUT)

## Schemas da API
Arquivos:
- `backend/app/schemas/feature_flag.py`

Schemas:
- `FeatureFlagCreate`: payload de criacao
- `FeatureFlagUpdate`: payload de atualizacao parcial
- `FeatureFlagRead`: resposta padrao

Exemplo de payload de criacao:
```json
{
  "name_flag": "habilitar_novo_formulario",
  "is_enabled": true,
  "status": "beta",
  "strategy": "liberar_para_grupo_a; rollout=25%; regra: idade>=5",
  "variation": "A",
  "created_by": 10,
  "updated_by": 10
}
```

## Regras de persistencia
Controller:
- arquivo: `backend/app/controllers/feature_flag.py`

Funcoes:
- `create_feature_flag`: cria e salva a feature
- `get_feature_flag`: busca por ID
- `list_feature_flags`: lista com paginacao
- `update_feature_flag`: atualiza campos presentes no payload
- `delete_feature_flag`: remove o registro

## Rotas da API
Base URL: `/api/feature-flags`
Arquivo das rotas: `backend/app/routes/feature_flag.py`

### 1) POST /api/feature-flags/
Cria uma feature flag.

Request body:
- `FeatureFlagCreate`

Response:
- 201 com `FeatureFlagRead`

Exemplo de resposta:
```json
{
  "id": 1,
  "name_flag": "habilitar_novo_formulario",
  "is_enabled": true,
  "status": "beta",
  "strategy": "liberar_para_grupo_a; rollout=25%; regra: idade>=5",
  "variation": "A",
  "created_at": "2025-01-21T10:00:00Z",
  "updated_at": "2025-01-21T10:00:00Z",
  "created_by": 10,
  "updated_by": 10
}
```

### 2) GET /api/feature-flags/
Lista todas as feature flags.

Query params:
- `skip` (default 0)
- `limit` (default 100)

Response:
- 200 com lista de `FeatureFlagRead`

### 3) GET /api/feature-flags/{feature_flag_id}
Busca uma feature flag pelo ID.

Response:
- 200 com `FeatureFlagRead`
- 404 se nao encontrada

### 4) PUT /api/feature-flags/{feature_flag_id}
Atualiza uma feature flag existente.

Request body:
- `FeatureFlagUpdate` (parcial)
- `updated_by` obrigatorio

Response:
- 200 com `FeatureFlagRead`
- 404 se nao encontrada
- 422 se `updated_by` nao for informado

### 5) DELETE /api/feature-flags/{feature_flag_id}
Remove uma feature flag.

Response:
- 204 sem conteudo
- 404 se nao encontrada

## Erros comuns
- 404: feature flag nao encontrada
- 422: `updated_by` nao informado em atualizacao
- 500: erro inesperado no banco ou na API

## Observacoes finais
- As migrations garantem que a tabela exista antes de usar as rotas.
- Se novas colunas forem adicionadas, e necessario criar migration.
- As rotas aparecem no `/docs` e `/redoc` do FastAPI.

## Dados iniciais (seed automatico)
Existe uma migration que popula automaticamente a tabela quando ela estiver vazia. Isso garante que, em um banco novo, as flags iniciais ja estejam disponiveis sem insercao manual.

Valores inseridos:
1) average_user
   - is_enabled: true
   - status: active
   - strategy: restricted_access
   - variation: {"percentage": 25, "target_group": "standard_users"}

2) admin_super
   - is_enabled: true
   - status: active
   - strategy: unrestricted_access
   - variation: {"allowed_roles": ["admin", "superadmin"], "visible_logs": true}

3) professional_tools
   - is_enabled: true
   - status: active
   - strategy: role_based_access
   - variation: {"features": ["advanced_analytics", "bulk_export"], "allowed_roles": ["pro", "specialist"]}
