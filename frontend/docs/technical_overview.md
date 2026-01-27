# Documentacao Tecnica (Frontend)

Este documento descreve o stack tecnico, bibliotecas usadas, motivacoes e estrategias adotadas no frontend.

## Framework e Ferramentas
### React + Vite + TypeScript
- **React**: construcao de interfaces por componentes.
- **Vite**: servidor rapido, build eficiente, configuracao simples.
- **TypeScript**: reduz erros com tipagem e melhora manutencao.

**Por que usar?**
- React e o padrao mais comum no mercado.
- Vite e rapido e leve para desenvolvimento.
- TypeScript evita bugs em tempo de desenvolvimento.

## Bibliotecas
### react-router-dom
- **Uso**: navegação entre paginas (`/`, `/criar-conta`, `/painel`).
- **Motivo**: SPA precisa de controle de rotas no frontend.

## Estrategias arquiteturais
### DDD (Domain-Driven Design) simplificado
- Estrutura por modulos: `auth`, `users`, `addresses`.
- Cada modulo contem suas telas e regras.
- Evita que tudo fique em um unico lugar e facilita manutencao.

### Separacao por camadas
- `modules/*/ui`: telas e componentes
- `shared`: codigo reutilizavel (servicos, utils, estilos)

### Variaveis de ambiente centralizadas
- `.env` com `VITE_API_BASE_URL`
- `env.ts` centraliza leitura e evita espalhar config no codigo

## Estrategias de integracao com backend
No fluxo de cadastro:
1) Cria endereco (`POST /api/addresses/`)
2) Busca feature flags (`GET /api/feature-flags`)
3) Cria usuario (`POST /api/users/`)

**Motivo**: garantir que o usuario seja criado apenas depois do endereco e da regra de role.

## Estrategia de feedback
- Logs de `console.info` e `console.error` no fluxo de cadastro e login
- Mensagem de erro mostrada na tela para o usuario

## Padroes de UI
- Cards com bordas arredondadas
- Formulario em grid responsivo
- Cores inspiradas no autismo

## Onde tudo fica
- `src/App.tsx`: rotas
- `src/modules/auth/ui`: telas de login/cadastro/painel
- `src/shared/services/env.ts`: config de API
- `src/index.css` e `src/App.css`: estilos globais
