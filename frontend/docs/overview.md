# Visao Geral do Frontend

O frontend e uma SPA em React + Vite + TypeScript. A arquitetura segue DDD por modulos e separa responsabilidades em camadas.

Principais pastas:
- `src/app`: configuracoes globais
- `src/shared`: componentes e utilitarios reutilizaveis
- `src/modules`: features por dominio (auth, users, addresses, etc.)

A pagina inicial (login) esta em `src/modules/auth/ui/LoginPage.tsx`.
A pagina de cadastro esta em `src/modules/auth/ui/SignupPage.tsx`.
As rotas ficam em `src/App.tsx`.
Os assets visuais ficam em `src/assets/`.
