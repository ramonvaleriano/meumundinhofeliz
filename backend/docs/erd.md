# ERD (Mapa de Entidades)

Este mapa descreve as principais tabelas e suas relacoes.

## Tabelas
- `address`
- `profile_type`
- `feature_flag`
- `users`
- `user_profile_type`

## Relacoes (diagrama ASCII)
```
address (1) <----- users (N)
   id                 address

users (1) ----< user_profile_type (N) >---- (1) profile_type
   id                 user_id                    id
                      profile_type_id
```

## Observacoes
- `feature_flag` nao tem relacao direta com `users`; o campo `role` em `users` guarda IDs de feature_flags.
- `user_profile_type` e tabela de associacao N:N entre users e profile_type.
