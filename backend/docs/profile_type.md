# Tabela ProfileType (Tipo de Perfil)

Este documento descreve a tabela `profile_type`, seu schema, objetivos e todas as rotas do CRUD expostas pela API.

## Objetivo
Armazenar tipos de perfis de usuario (ex: profissionais, pais, especialistas). Essa tabela pode ser usada para classificar usuarios em telas e fluxos da aplicacao.

## Estrutura da tabela
Tabela: `profile_type`

Colunas:
- `id` (integer, PK, auto incremental)
- `user_type` (string, obrigatorio)

Model:
- arquivo: `backend/app/models/profile_type.py`

## Regras de validacao
No momento, as validacoes sao simples:
- `user_type` e obrigatorio
- tipo string

## Schemas da API
Arquivos:
- `backend/app/schemas/profile_type.py`

Schemas:
- `ProfileTypeCreate`: payload de criacao
- `ProfileTypeUpdate`: payload de atualizacao parcial
- `ProfileTypeRead`: resposta padrao

Exemplo de payload de criacao:
```json
{
  "user_type": "Neuropediatra"
}
```

## Regras de persistencia
Controller:
- arquivo: `backend/app/controllers/profile_type.py`

Funcoes:
- `create_profile_type`: cria e salva o tipo de perfil
- `get_profile_type`: busca por ID
- `list_profile_types`: lista com paginacao
- `update_profile_type`: atualiza campos presentes no payload
- `delete_profile_type`: remove o registro

## Rotas da API
Base URL: `/api/profile-types`
Arquivo das rotas: `backend/app/routes/profile_type.py`

### 1) POST /api/profile-types/
Cria um tipo de perfil.

Request body:
- `ProfileTypeCreate`

Response:
- 201 com `ProfileTypeRead`

Exemplo de resposta:
```json
{
  "id": 1,
  "user_type": "Neuropediatra"
}
```

### 2) GET /api/profile-types/
Lista todos os tipos de perfil.

Query params:
- `skip` (default 0)
- `limit` (default 100)

Response:
- 200 com lista de `ProfileTypeRead`

### 2.1) GET /api/profile-types/all
Lista todos os tipos de perfil sem paginação/filtros.

Response:
- 200 com lista completa de `ProfileTypeRead`

Observacao:
- A rota `/all` deve ficar antes de `/{profile_type_id}` para evitar conflito.

### 3) GET /api/profile-types/{profile_type_id}
Busca um tipo de perfil pelo ID.

Response:
- 200 com `ProfileTypeRead`
- 404 se nao encontrado

### 4) PUT /api/profile-types/{profile_type_id}
Atualiza um tipo de perfil existente.

Request body:
- `ProfileTypeUpdate` (parcial)

Response:
- 200 com `ProfileTypeRead`
- 404 se nao encontrado

### 5) DELETE /api/profile-types/{profile_type_id}
Remove um tipo de perfil.

Response:
- 204 sem conteudo
- 404 se nao encontrado

## Erros comuns
- 404: perfil nao encontrado
- 500: erro inesperado no banco ou na API

## Observacoes finais
- As migrations garantem que a tabela exista antes de usar as rotas.
- Se novas colunas forem adicionadas, e necessario criar migration.
- As rotas aparecem no `/docs` e `/redoc` do FastAPI.

## Dados iniciais (seed automatico)
Existe uma migration que popula automaticamente a tabela quando ela estiver vazia. Isso garante que, em um banco novo, os tipos de perfil ja estejam disponiveis sem necessidade de insercao manual.

Lista de valores inseridos:
- Médico(a)
- Pediatra
- Neuropediatra
- Neurologista
- Psiquiatra
- Psiquiatra Infantil
- Geneticista
- Médico(a) de Família e Comunidade
- Médico(a) do Desenvolvimento e Comportamento (quando disponível)
- Gastroenterologista
- Alergista/Imunologista
- Otorrinolaringologista
- Oftalmologista
- Pneumologista
- Endocrinologista
- Dermatologista
- Ortopedista
- Médico(a) do Sono
- Fisiatra (Medicina Física e Reabilitação)
- Psicólogo(a)
- Neuropsicólogo(a)
- Psicoterapeuta
- Analista do Comportamento (ABA)
- Supervisor(a) ABA
- Terapeuta ABA
- Acompanhante Terapêutico(a) (AT)
- Psicopedagogo(a)
- Fonoaudiólogo(a)
- Terapeuta Ocupacional
- Fisioterapeuta
- Psicomotricista
- Terapeuta Psicomotor(a)
- Educador(a) Físico(a)
- Professor(a) de Educação Física Adaptada
- Especialista em Comunicação Alternativa e Aumentativa (CAA)
- Intérprete de Libras
- Guia-intérprete (quando aplicável)
- Nutricionista
- Terapeuta Alimentar (seletividade/introdução alimentar - quando houver essa função no serviço)
- Fonoaudiólogo(a) (disfagia/alimentação - quando aplicável)
- Enfermeiro(a)
- Técnico(a) de Enfermagem
- Cirurgião(ã)-Dentista
- Odontopediatra
- Assistente Social
- Professor(a)
- Professor(a) Regente
- Professor(a) de Educação Especial
- Professor(a) do AEE (Atendimento Educacional Especializado)
- Coordenador(a) Pedagógico(a)
- Orientador(a) Educacional
- Psicólogo(a) Escolar
- Mediador(a) Escolar
- Acompanhante Escolar
- Cuidador(a) Escolar
- Tutor(a) Escolar (quando usado pela instituição)
- Professor(a) de Apoio
- Musicoterapeuta
- Arteterapeuta
- Terapeuta de Integração Sensorial (especialização/ênfase em TO)
- Equoterapeuta (quando praticado em programas específicos)
- Terapeuta Assistido por Animais (quando existente no serviço)
- Farmacêutico(a) (quando há acompanhamento de medicação)
- Fonoaudiólogo(a) Educacional (quando aplicável)
- Terapeuta Familiar (quando aplicável)
- País
- Responsável Legal
