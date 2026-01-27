# Arquitetura (DDD simplificado)

A organizacao do frontend segue uma ideia de DDD (Domain Driven Design). Isso evita bagunca e facilita a manutencao.

## Estrutura
```
src/
  app/
    routes/        # (reservado) configuracoes de rotas
    providers/     # (reservado) providers globais
    styles/        # (reservado) estilos globais
  shared/
    components/    # componentes reutilizaveis (botoes, inputs)
    hooks/         # hooks compartilhados
    lib/           # bibliotecas auxiliares
    services/      # integracoes (ex: env, http client)
    styles/        # tokens visuais (cores, fontes)
    types/         # tipos globais
    utils/         # funcoes utilitarias
  modules/
    auth/
      domain/      # regras do dominio de autenticacao
      application/ # casos de uso
      infra/       # integracoes externas
      ui/          # telas e componentes
    users/ ...
    addresses/ ...
    featureFlags/ ...
    profileTypes/ ...
```

## Onde estamos usando hoje
- `modules/auth/ui` contem as telas de Login e Criar Conta.
- `shared/services/env.ts` centraliza as variaveis do `.env`.
- `App.tsx` concentra as rotas atuais.

## Por que isso ajuda
- Cada modulo fica isolado.
- Mudancas em um modulo nao quebram outro.
- Fica facil criar novas telas sem bagunçar o projeto.
