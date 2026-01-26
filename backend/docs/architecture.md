# Arquitetura do Backend

## Visao geral
O backend segue um padrao MVC adaptado ao FastAPI:
- **Models**: definicao das tabelas (SQLAlchemy)
- **Schemas**: contratos de entrada/saida (Pydantic)
- **Controllers**: regras de negocio e acesso a dados
- **Routes**: endpoints HTTP
- **Services**: utilitarios de negocio (criptografia, identidade, etc.)
- **Core**: configuracoes, banco e migrations

## Fluxo de execucao
1) `main.py` inicia o FastAPI e registra as rotas.
2) No startup (`lifespan`) o sistema:
   - cria o banco se nao existir
   - executa as migrations ate `head`
3) A API fica pronta para receber requisicoes.

## Assincrono
- As rotas usam `async def`.
- O banco usa `SQLAlchemy Async` + `asyncpg`.
- O Alembic roda em modo sincrono usando `database_url_sync`.

## Startup e migrations
Arquivos:
- `backend/main.py`
- `backend/app/core/database.py`
- `backend/app/core/migrations.py`

No startup:
- `ensure_database_exists()` cria o banco
- `run_migrations()` aplica todas as migrations pendentes

## Convencoes
- Controllers encapsulam regras de negocio
- Schemas definem exemplos e validacoes de payload
- Migrations registram toda alteracao de tabela
