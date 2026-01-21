# Migrations e validacao automatica de banco

Este documento explica como o projeto trata criacao, atualizacao e validacao de tabelas usando Alembic, e como isso roda automaticamente quando a API inicia.

## O que e o Alembic
Alembic e a ferramenta oficial de migrations do SQLAlchemy. Ela mantem um historico versionado das mudancas do schema do banco de dados (tabelas, colunas, indices, constraints). Cada mudanca e registrada em um arquivo de revision dentro de `backend/alembic/versions`.

Beneficios no projeto:
- Versionamento do schema (tudo fica rastreavel)
- Atualizacao automatica do banco para o estado esperado
- Controle de historico para testes e ambientes diferentes

## Estrutura de configuracao
Arquivos principais:
- `backend/alembic.ini`: configuracao base do Alembic
- `backend/alembic/env.py`: integra o Alembic com o projeto e carrega os models
- `backend/app/core/migrations.py`: executa `alembic upgrade head` via codigo
- `backend/app/core/database.py`: cria o banco, se ele nao existir
- `backend/app/core/config.py`: deriva a URL sincrona para o Alembic quando a URL principal usa asyncpg

## Validacao e criacao do banco
O projeto faz duas coisas automaticamente ao iniciar:
1) Verifica se o banco existe e cria se nao existir.
2) Executa as migrations pendentes ate a ultima revision.

Esse fluxo roda no startup do FastAPI usando lifespan:
- arquivo: `backend/main.py`
- funcao: `lifespan` chama `ensure_database_exists()` e `run_migrations()`

Isso garante que qualquer mudanca nos models, quando convertida em migration, sera aplicada automaticamente ao iniciar a API.

## Como criar novas migrations
Quando voce cria ou altera models em `backend/app/models`, gere uma migration:

```bash
cd backend
source .venv/bin/activate
alembic revision --autogenerate -m "descricao"
```

Depois disso, basta iniciar a API normalmente que ela aplicara as migrations automaticamente.

## Onde as migrations sao aplicadas
No startup do app:
- arquivo: `backend/main.py`
- ponto de execucao: `lifespan` (antes de a API aceitar requisicoes)

Isso significa que:
- ao rodar `python3 main.py`, o banco e atualizado
- ao rodar `uvicorn main:app --reload`, o banco e atualizado

## Detalhes importantes
- O usuario do `DATABASE_URL` precisa ter permissao para criar banco e alterar schema.
- A API usa `asyncpg` (URL async), mas o Alembic roda com URL sincronizada automaticamente.
- Mantenha `psycopg2-binary` no ambiente para o Alembic e para a criacao automatica do banco.
- Se houver erro de migration, a API pode nao iniciar. A falha aparece no log do servidor.
- O Alembic so aplica migrations existentes. Ele nao cria migrations automaticamente. Voce precisa gerar o arquivo com `alembic revision --autogenerate`.

## Fluxo recomendado
1) Atualizar/editar o model
2) Gerar migration
3) Subir a API e deixar o Alembic aplicar

## Exemplo de fluxo completo
1) Edite um model, por exemplo `Address`
2) Gere migration:
```bash
alembic revision --autogenerate -m "add campo"
```
3) Rode o servidor:
```bash
python3 main.py
```
4) A migration e aplicada automaticamente

## Por que isso evita problemas
Sem migrations, o banco fica inconsistente e pode gerar erros em tempo de execucao. Com esse fluxo:
- O banco sempre reflete o schema esperado pelo codigo
- O deploy fica previsivel
- Mudancas sao controladas e auditaveis
