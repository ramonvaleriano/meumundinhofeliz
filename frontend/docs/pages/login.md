# Pagina: Login

Arquivo:
- `src/modules/auth/ui/LoginPage.tsx`

## Como chegar
- Acesso direto pela rota `/`
- Esta e a pagina inicial do sistema

## Objetivo
Autenticar um usuario e redirecionar para o painel interno.

## Campos
- E-mail
- Senha

## Requisicoes
### POST /api/auth/login
- URL base: `VITE_API_BASE_URL` (ex: `http://localhost:8000`)
- Payload enviado:
```json
{
  "email": "usuario@email.com",
  "password": "Senha@123"
}
```

## Resposta esperada (sucesso)
```json
{
  "token": "..."
}
```

## Regras de negocio
- Se autenticar com sucesso, redireciona para `/painel`.
- Se falhar, mostra mensagem de erro na pagina e nao navega.

## Logs no frontend
- `console.info` em sucesso
- `console.error` em erro

## Diagrama simples
Ver: `docs/pages/diagramas.md`
