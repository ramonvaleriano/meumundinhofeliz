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

### Regras de integracao (backend)
1) Cria endereco em `POST /api/addresses/`
2) Busca feature flags em `GET /api/feature-flags/?skip=0&limit=100`
   - Se perfil for **País** ou **Responsável Legal** -> usa `average_user`
   - Caso contrario -> usa `professional_tools`
3) Cria usuario em `POST /api/users/` com:
   - `is_active = true`
   - `is_verified = true`
   - `address = id` retornado do endereco
   - `role = [id_da_feature_flag]`
   - `last_login = new Date().toISOString()`
Se qualquer passo falhar, mostra erro e permanece na pagina.

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
4) Se tudo der certo, vai para `/painel`

Agora ja existe envio para backend no cadastro inicial.

## 3) Painel
Arquivo:
- `src/modules/auth/ui/DashboardPage.tsx`

Pagina placeholder para o painel interno.
