# Regras de Negocio (Resumo)

## Users
- `uuid` e gerado automaticamente via `UserIdentityCipher.create_hash`.
- `token` e gerado automaticamente via `UserIdentityCipher.create_token`.
- `password` e criptografado via `PasswordCipher`.
- `role` default depende da feature flag.
- `updated_by` e obrigatorio em updates.

## Address
- Campos obrigatorios: cep, estado, bairro, tipo_logradouro, logradouro, numero.

## ProfileType
- Lista de tipos pre-seeded.
- Endpoint `/all` retorna todos sem paginacao.

## FeatureFlag
- `is_enabled` default true.
- `strategy` obrigatorio.
- `updated_by` obrigatorio em update.
- Seeds de flags iniciais.

## UserProfileType
- FK valida: user_id e profile_type_id devem existir.
- On delete cascade.

## Auth
- Login gera novo token e atualiza `last_login`.
- Refresh valida token e UUID.
