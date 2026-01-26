# Visao Geral do Frontend

O frontend e uma SPA em React + Vite + TypeScript. A arquitetura segue DDD por modulos e separa responsabilidades em camadas.

Principais pastas:
- `src/app`: configuracoes globais
- `src/shared`: componentes e utilitarios reutilizaveis
- `src/modules`: features por dominio (auth, users, addresses, etc.)

A primeira tela esta em `src/App.tsx` (pagina inicial).
