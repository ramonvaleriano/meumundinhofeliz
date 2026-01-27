# Guia Rapido (Leigo)

Este guia explica como rodar o sistema sem termos tecnicos.

## 1) Rodar o backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

Quando o backend estiver rodando, abra no navegador:
- http://localhost:8000/docs (documentacao interativa)

## 2) Rodar o frontend
```bash
cd frontend
npm install
npm run dev
```

Abra no navegador:
- http://localhost:5173

## 3) Teste simples
Abra no navegador:
- http://localhost:8000/api/health

Se aparecer `{"status": "ok"}`, esta funcionando.

## 4) O que fazer se der erro
Leia o arquivo:
- `backend/docs/troubleshooting.md`
