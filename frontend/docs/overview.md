# Visao Geral

Este frontend e uma SPA (Single Page Application) feita com React + Vite + TypeScript.

## O que isso significa
- **SPA**: a pagina nao recarrega a cada clique; o React troca o conteudo.
- **Vite**: servidor rapido para desenvolvimento e build.
- **TypeScript**: adiciona tipos para reduzir erros.

## Pastas importantes
- `src/`: codigo do app
- `src/modules/`: funcionalidades separadas por modulo (auth, users, etc.)
- `src/shared/`: componentes e utilitarios reutilizaveis
- `src/assets/`: imagens (logo e fundo)
- `src/App.tsx`: definicao das rotas
- `src/main.tsx`: ponto de entrada do React

## Rotas atuais
- `/` -> Login
- `/criar-conta` -> Cadastro inicial
- `/painel` -> Placeholder do painel interno

## Integração inicial com backend
- O cadastro inicial carrega **Tipo de Perfil** da API.
- O cadastro inicial cria endereco, busca feature flag e cria usuario.
- O login chama `POST /api/auth/login` e navega para `/painel` em sucesso.
- A URL da API vem do `.env`.

Arquivos principais:
- `src/shared/services/env.ts`
- `src/modules/auth/ui/SignupPage.tsx`
