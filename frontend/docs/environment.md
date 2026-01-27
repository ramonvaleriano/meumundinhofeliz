# Variaveis de Ambiente (Frontend)

O frontend usa variaveis com prefixo `VITE_`. Isso e obrigatorio no Vite.

## Arquivo
- `frontend/.env`

## Variaveis usadas
- `VITE_API_BASE_URL`: URL base da API (ex: `http://localhost:8000`)

## Como o codigo lê
Todas as variaveis estao centralizadas em:
- `frontend/src/shared/services/env.ts`

Exemplo:
```ts
import { env } from '@/shared/services/env'

fetch(`${env.apiBaseUrl}/api/profile-types/all`)
```

## Importante
Sempre reinicie o `npm run dev` ao alterar o `.env`.
