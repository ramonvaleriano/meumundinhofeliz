# Padroes de Erro (Frontend)

Este arquivo descreve como o frontend mostra erros para o usuario.

## Cadastro
- Se falhar ao criar endereco: mostra mensagem "Erro ao criar endereco"
- Se falhar ao buscar feature flags: mostra mensagem "Erro ao buscar feature flags"
- Se falhar ao criar usuario: mostra mensagem "Erro ao criar usuario"

## Login
- Se falhar no login: mostra erro retornado pela API

## Comportamento
- Em erro, o usuario permanece na pagina
- A mensagem aparece na tela (banner vermelho)
- Logs sao enviados para o console (info/error)
