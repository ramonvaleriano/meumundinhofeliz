# Diagramas Simples

## Fluxo geral
```
[Login] ---> (sucesso) ---> [Painel]
   |               
   +-- "Criar conta" ---> [Cadastro]

[Cadastro] -> cria endereco -> busca feature flags -> cria usuario -> [Painel]
```

## Login
```
Usuario digita email/senha
        |
        v
POST /api/auth/login
        |
   +----+----+
   |         |
 sucesso   erro
   |         |
   v         v
 /painel   mostrar mensagem
```

## Cadastro
```
Formulario preenchido
        |
        v
POST /api/addresses/
        |
        v
GET /api/feature-flags
        |
        v
POST /api/users/
        |
   +----+----+
   |         |
 sucesso   erro
   |         |
   v         v
 /painel   mostrar mensagem
```
