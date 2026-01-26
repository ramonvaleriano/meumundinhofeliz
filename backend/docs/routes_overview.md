# Visao Geral de Rotas

Base URL local: `http://127.0.0.1:8000`

## Healthcheck
- `GET /` -> status da API
- `GET /api/health` -> status do servidor
- `GET /api/db/health` -> status do banco

## Auth
- `POST /api/auth/login`
- `POST /api/auth/refresh?uuid=...&token=...`

## Address
- `POST /api/addresses/`
- `GET /api/addresses/`
- `GET /api/addresses/{id}`
- `PUT /api/addresses/{id}`
- `DELETE /api/addresses/{id}`

## ProfileType
- `POST /api/profile-types/`
- `GET /api/profile-types/`
- `GET /api/profile-types/{id}`
- `PUT /api/profile-types/{id}`
- `DELETE /api/profile-types/{id}`

## FeatureFlag
- `POST /api/feature-flags/`
- `GET /api/feature-flags/`
- `GET /api/feature-flags/{id}`
- `PUT /api/feature-flags/{id}`
- `DELETE /api/feature-flags/{id}`

## Users
- `POST /api/users/`
- `GET /api/users/`
- `GET /api/users/{id}`
- `PUT /api/users/{id}`
- `PATCH /api/users/{id}`
- `DELETE /api/users/{id}`

## Documentacao automatica
- `/docs` (Swagger)
- `/redoc`
