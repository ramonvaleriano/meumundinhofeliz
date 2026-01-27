# Paginas e Fluxo

## 1) Login (pagina inicial)
Arquivo:
- `src/modules/auth/ui/LoginPage.tsx`

Conteudo:
- Logo e titulo "ConectVida"
- Texto introdutorio
- Formulario de login (email e senha)
- Link "Esqueci minha senha" (placeholder)
- Botao "Criar conta" que leva para `/criar-conta`

## 2) Criar Conta
Arquivo:
- `src/modules/auth/ui/SignupPage.tsx`

### Sessao: Dados pessoais
Campos obrigatorios:
- Nome
- Sobrenome
- Data de nascimento
- CPF
- Celular
- E-mail
- Senha

### Sessao: Tipo de Perfil
- Campo select que carrega dados da API
- Endpoint: `GET /api/profile-types/all`
- Exibe o `user_type`
- Guarda `id` e `user_type` no estado

### Sessao: Endereco
Campos:
- CEP
- Tipo de logradouro (select)
- Logradouro
- Bairro
- Estado
- Numero
- Complemento (opcional)
- Referencia (opcional)

## Fluxo atual
1) Usuario entra em `/`
2) Clica em "Criar conta"
3) Preenche formulario em `/criar-conta`

Sem envio para backend por enquanto (apenas UI).
