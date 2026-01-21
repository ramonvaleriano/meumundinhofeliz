# Backend - Documentacao Inicial

## Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

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
  DATABASE_URL="postgresql+psycopg2://postgres@localhost:5432/meumundinho"
