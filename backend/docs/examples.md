# Exemplos de Requisicoes (Desenvolvedor)

Este arquivo traz exemplos prontos de requests e respostas.

## Address
### Criar
```bash
curl -X POST http://localhost:8000/api/addresses/ \
  -H 'Content-Type: application/json' \
  -d '{
    "cep": "01310-200",
    "estado": "SP",
    "bairro": "Bela Vista",
    "tipo_logradouro": "Avenida",
    "logradouro": "Paulista",
    "numero": "1000",
    "complemento": "Apto 101",
    "referencia": "Proximo ao MASP"
  }'
```

## ProfileType
### Listar todos (sem paginacao)
```bash
curl http://localhost:8000/api/profile-types/all
```

## FeatureFlag
### Criar
```bash
curl -X POST http://localhost:8000/api/feature-flags/ \
  -H 'Content-Type: application/json' \
  -d '{
    "name_flag": "professional_tools",
    "is_enabled": true,
    "status": "active",
    "strategy": "role_based_access",
    "variation": "{\"features\": [\"advanced_analytics\", \"bulk_export\"], \"allowed_roles\": [\"pro\", \"specialist\"]}",
    "created_by": 1,
    "updated_by": 1
  }'
```

## Users
### Criar
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Ana",
    "surname": "Silva",
    "email": "ana@email.com",
    "cpf": "123.456.789-00",
    "cellphone": "(11) 99999-9999",
    "birth_date": "2000-01-01",
    "password": "Senha@123",
    "is_active": true,
    "is_verified": false,
    "role": [1]
  }'
```

## Auth
### Login
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email": "ana@email.com", "password": "Senha@123"}'
```

### Refresh
```bash
curl -X POST "http://localhost:8000/api/auth/refresh?uuid=SEU_UUID&token=SEU_TOKEN"
```
