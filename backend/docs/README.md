# Backend - Documentacao Inicial

## Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- asyncpg

## Documentos detalhados
- Migrations: docs/migrations.md
- Tabela Address: docs/address.md
- Servico de Criptografia: docs/crypto_service.md
- Servico de Identidade: docs/user_identity_service.md
- Tabela FeatureFlag: docs/feature_flag.md
- Tabela ProfileType: docs/profile_type.md

## Estrutura atual
- app/core: configuracao e conexao com banco
- app/routes: rotas da API
- app/models: reservado para models (ORM)
- app/schemas: reservado para schemas (Pydantic)
- app/controllers: reservado para regras de negocio

## Executar
1) Criar e ativar o venv
2) Instalar dependencias
3) Subir o servidor

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Endpoints
Base URL local: `http://127.0.0.1:8000`

### 1) GET /
Retorna o status basico da API.

Exemplo de resposta:
```json
{"status":"ok","message":"API online"}
```

### 2) GET /api/health
Healthcheck geral da API. Indica se o servidor esta ativo.

Exemplo de resposta:
```json
{"status":"ok"}
```

### 3) GET /api/db/health
Healthcheck do banco de dados. Verifica se a conexao com o Postgres esta funcionando.

Exemplo de resposta:
```json
{"status":"ok","database":"up"}
```

Possiveis erros:
- 500: indica que o banco esta indisponivel ou a credencial esta incorreta.

## Configuracao
- .env com DATABASE_URL
- Exemplo:
  DATABASE_URL="postgresql+asyncpg://postgres@localhost:5432/meumundinho"

## Migrations (Alembic)
O projeto ja esta configurado para migrations automaticas via Alembic.

Comandos basicos:
```bash
cd backend
source .venv/bin/activate
alembic upgrade head
```

Para criar novas migrations (quando adicionar/alterar models):
```bash
alembic revision --autogenerate -m "descricao"
```
