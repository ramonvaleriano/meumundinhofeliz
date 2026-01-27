# Variaveis de Ambiente (Frontend)

O frontend usa variaveis com prefixo `VITE_`.

## Variaveis
- `VITE_API_BASE_URL`: URL base da API (ex: `http://localhost:8000`)

## Arquivo
- `frontend/.env`

## Leitura no codigo
As variaveis sao acessadas via `import.meta.env` e centralizadas em:
- `frontend/src/shared/services/env.ts`

Exemplo:
```ts
import { env } from '@/shared/services/env'

fetch(`${env.apiBaseUrl}/api/health`)
```
