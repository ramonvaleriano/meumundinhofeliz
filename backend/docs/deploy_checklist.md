# Checklist de Deploy

## 1) Variaveis de ambiente
- `DATABASE_URL`
- `CRYPTO_KEY`
- `USER_HASH_KEY`
- `TOKEN_EXP_MINUTES`
- `ADMIN_*` (para seed inicial)

## 2) Banco
- Postgres rodando
- Permissoes para criar banco e alterar schema

## 3) Migrations
```bash
cd backend
source .venv/bin/activate
PYTHONPATH=. alembic upgrade head
```

## 4) API
```bash
python3 main.py
```

## 5) Validacoes basicas
- `GET /api/health`
- `GET /api/db/health`

## 6) Seeds
- `profile_type`
- `feature_flag`
- `users` (admin)

## Observacao
Se mudar um `revision id`, atualize a tabela `alembic_version`.
