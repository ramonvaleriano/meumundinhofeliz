# Pagina: Criar Conta

Arquivo:
- `src/modules/auth/ui/SignupPage.tsx`

## Como chegar
- Pela pagina inicial, clicando em "Criar conta"
- Acesso direto pela rota `/criar-conta`

## Objetivo
Criar um usuario novo e seus dados relacionados (endereco e role).

## Campos
### Dados pessoais
- Nome
- Sobrenome
- Data de nascimento
- CPF
- Celular
- E-mail
- Senha

### Tipo de Perfil
- Select carregado via API

### Endereco
- CEP
- Tipo de logradouro
- Logradouro
- Bairro
- Estado
- Numero
- Complemento (opcional)
- Referencia (opcional)

## Requisicoes (fluxo)
### 1) POST /api/addresses/
Payload enviado:
```json
{
  "cep": "01000-000",
  "estado": "SP",
  "bairro": "Centro",
  "tipo_logradouro": "Rua",
  "logradouro": "Rua das Flores",
  "numero": "123",
  "complemento": null,
  "referencia": null
}
```

Resposta esperada:
```json
{
  "id": 1,
  "cep": "01000-000",
  "estado": "SP",
  "bairro": "Centro",
  "tipo_logradouro": "Rua",
  "logradouro": "Rua das Flores",
  "numero": "123",
  "complemento": null,
  "referencia": null
}
```

### 2) GET /api/feature-flags/?skip=0&limit=100
Seleciona o id da feature flag:
- **average_user** se o perfil for "País" ou "Responsável Legal"
- **professional_tools** nos demais casos

### 3) POST /api/users/
Payload enviado (exemplo):
```json
{
  "name": "Ana",
  "surname": "Silva",
  "email": "ana@email.com",
  "cpf": "123.456.789-00",
  "cellphone": "(11) 99999-9999",
  "birth_date": "2000-01-01",
  "password": "Senha@123",
  "address": 1,
  "is_active": true,
  "is_verified": true,
  "role": [2],
  "last_login": "2026-01-27T18:47:07.608Z"
}
```

Resposta esperada (sucesso):
```json
{
  "id": 10,
  "name": "Ana",
  "surname": "Silva",
  "email": "ana@email.com",
  "cpf": "123.456.789-00",
  "cellphone": "(11) 99999-9999",
  "birth_date": "2000-01-01",
  "address": 1,
  "role": [2]
}
```

## Regras de negocio
- Se qualquer passo falhar, mostra erro e permanece na pagina.
- Se tudo der certo, redireciona para `/painel`.

## Logs no frontend
- `console.info` em etapas de sucesso
- `console.error` em erros

## Diagrama simples
Ver: `docs/pages/diagramas.md`
