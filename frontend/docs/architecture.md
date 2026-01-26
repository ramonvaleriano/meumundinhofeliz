# Arquitetura (DDD)

Estrutura:
```
src/
  app/
    routes/        # roteamento (ainda simples, centralizado em App.tsx)
    providers/     # providers globais
    styles/        # estilos globais
  shared/
    components/    # componentes reutilizaveis
    hooks/         # hooks compartilhados
    lib/           # libs auxiliares
    services/      # clientes http, config
    styles/        # tokens de UI
    types/         # tipos globais
    utils/         # funcoes utilitarias
  modules/
    auth/
      domain/      # entidades, regras
      application/ # casos de uso
      infra/       # gateways/clients
      ui/          # telas e componentes
    users/ ...
    addresses/ ...
    featureFlags/ ...
    profileTypes/ ...
```

Cada modulo encapsula o que pertence ao dominio, evitando acoplamento.
