# Setup do Backend

## Requisitos
- Python 3.10+
- Postgres 14+

## Criar ambiente virtual
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
```

## Instalar dependencias
```bash
pip install -r requirements.txt
```

## Configurar `.env`
Crie/edite `backend/.env` com as variaveis obrigatorias. Veja `docs/environment.md`.

## Rodar a aplicacao
```bash
python3 main.py
```

## Rodar migrations manualmente
```bash
PYTHONPATH=. alembic upgrade head
```
