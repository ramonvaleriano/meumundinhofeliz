# Tabela Address (Endereco)

Este documento descreve completamente a tabela `address`, seu schema, objetivos, e todas as rotas expostas pela API.

## Objetivo
Armazenar enderecos relacionados a pacientes, responsaveis ou unidades. A tabela foi criada com campos suficientes para enderecos brasileiros e contempla campos obrigatorios e opcionais.

## Estrutura da tabela
Tabela: `address`

Colunas:
- `id` (integer, PK, auto incremental)
- `cep` (string, obrigatorio)
- `estado` (string, obrigatorio)
- `bairro` (string, obrigatorio)
- `tipo_logradouro` (string, obrigatorio)
- `logradouro` (string, obrigatorio)
- `numero` (string, obrigatorio)
- `complemento` (string, opcional)
- `referencia` (string, opcional)

Model:
- arquivo: `backend/app/models/address.py`

## Regras de validacao
No momento as validacoes sao simples (apenas tipos e obrigatoriedade).
- Campos obrigatorios nao podem ser nulos
- Campos opcionais podem ser nulos

Se desejar, e possivel adicionar validacao de formato do CEP, tamanho maximo ou regras especificas.

## Schemas da API
Arquivos:
- `backend/app/schemas/address.py`

Schemas:
- `AddressCreate`: payload de criacao
- `AddressUpdate`: payload de atualizacao parcial
- `AddressRead`: resposta padrao

Exemplo de payload de criacao:
```json
{
  "cep": "01310-200",
  "estado": "SP",
  "bairro": "Bela Vista",
  "tipo_logradouro": "Avenida",
  "logradouro": "Paulista",
  "numero": "1000",
  "complemento": "Apto 101",
  "referencia": "Proximo ao MASP"
}
```

## Regras de persistencia
Controller:
- arquivo: `backend/app/controllers/address.py`

Funcoes:
- `create_address`: cria e salva o endereco
- `get_address`: busca por ID
- `list_addresses`: lista com paginacao
- `update_address`: atualiza campos presentes no payload
- `delete_address`: remove o registro

## Rotas da API
Base URL: `/api/addresses`
Arquivo das rotas: `backend/app/routes/address.py`

### 1) POST /api/addresses/
Cria um endereco.

Request body:
- `AddressCreate`

Response:
- 201 com `AddressRead`

Exemplo de resposta:
```json
{
  "id": 1,
  "cep": "01310-200",
  "estado": "SP",
  "bairro": "Bela Vista",
  "tipo_logradouro": "Avenida",
  "logradouro": "Paulista",
  "numero": "1000",
  "complemento": "Apto 101",
  "referencia": "Proximo ao MASP"
}
```

### 2) GET /api/addresses/
Lista todos os enderecos.

Query params:
- `skip` (default 0)
- `limit` (default 100)

Response:
- 200 com lista de `AddressRead`

### 3) GET /api/addresses/{address_id}
Busca um endereco pelo ID.

Response:
- 200 com `AddressRead`
- 404 se nao encontrado

### 4) PUT /api/addresses/{address_id}
Atualiza um endereco existente.

Request body:
- `AddressUpdate` (parcial)

Response:
- 200 com `AddressRead`
- 404 se nao encontrado

### 5) DELETE /api/addresses/{address_id}
Remove um endereco.

Response:
- 204 sem conteudo
- 404 se nao encontrado

## Erros comuns
- 404: endereco nao encontrado
- 500: erro inesperado no banco ou na API

## Observacoes finais
- As migrations garantem que a tabela exista antes de usar as rotas.
- Se novas colunas forem adicionadas, e necessario criar migration.
- As rotas ja estao documentadas no `/docs` e `/redoc` do FastAPI.
