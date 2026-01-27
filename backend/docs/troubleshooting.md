# Troubleshooting

Este documento reune problemas comuns encontrados durante o desenvolvimento e como corrigi-los. Ele complementa `docs/migrations.md` e pode ter informacoes repetidas para facilitar a consulta.

## 1) Alembic nao encontra o modulo `app`
**Erro:** `ModuleNotFoundError: No module named 'app'`

**Causa:** o `PYTHONPATH` nao inclui a raiz do backend.

**Solucao:**
```bash
cd backend
source .venv/bin/activate
PYTHONPATH=. alembic upgrade head
```

## 2) Migration rodou, mas a tabela nao atualiza
**Sintoma:** log diz que rodou, mas as colunas nao aparecem no banco.

**Causas comuns:**
- Conexao do DBeaver aponta para outra instância
- Cache de schema no DBeaver

**Verifique no terminal (WSL):**
```bash
psql -U postgres -d meumundinho -c "\d users"
```

**Atualize no DBeaver:**
- Clique com o botao direito na tabela `users` -> **Refresh**
- Ou reconecte a conexao

## 3) Erro de tamanho em `alembic_version`
**Erro:** `value too long for type character varying(32)`

**Causa:** o `revision id` tem mais de 32 caracteres.

**Solucao recomendada:**
- Renomear a revision para um id curto (ex: `add_cellphone_birthdate`).
- Atualizar o banco caso ja esteja registrado.

**Comando para ajustar no banco:**
```bash
psql -U postgres -d meumundinho -c "UPDATE alembic_version SET version_num='NOVO_ID' WHERE version_num='ID_ANTIGO';"
```

## 4) Erro: "Can't locate revision identified by ..."
**Causa:** o banco referencia um `revision` antigo que foi renomeado no codigo.

**Solucao:** atualize o `alembic_version` no banco:
```bash
psql -U postgres -d meumundinho -c "UPDATE alembic_version SET version_num='NOVO_ID' WHERE version_num='ID_ANTIGO';"
```

## 5) Seed nao insere dados
**Sintoma:** logs dizem que a migration rodou, mas a tabela continua vazia.

**Possiveis causas:**
- Tabela nao esta vazia (seed so roda se estiver vazia)
- Erro ao inicializar `PasswordCipher` ou `UserIdentityCipher`

**Verifique se o seed executou:**
```bash
psql -U postgres -d meumundinho -c "SELECT COUNT(*) FROM users;"
```

**Se a tabela estiver vazia, verifique chaves no .env:**
- `CRYPTO_KEY`
- `USER_HASH_KEY`

## 6) Seed falha por chave invalida do Fernet
**Erro:** `Fernet key must be 32 url-safe base64-encoded bytes`

**Solucao atual:** o projeto deriva a chave automaticamente via `derive_fernet_key`, entao qualquer string simples serve.

Verifique:
- `backend/app/utils/key_utils.py`
- `backend/app/services/crypto_service.py`

## 7) Banco diferente do backend
**Sintoma:** o backend faz migrations, mas no DBeaver nao aparece nada.

**Causa:** DBeaver conectado em outra instancia do Postgres (Windows vs WSL).

**Solucao:** use o IP do WSL e a porta correta. Veja `docs/setup.md` e `docs/environment.md`.

## Links
- Migrations: `docs/migrations.md`
- Setup: `docs/setup.md`
- Variaveis de ambiente: `docs/environment.md`
