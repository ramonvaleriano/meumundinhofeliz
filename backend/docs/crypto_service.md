# Servico de Criptografia (PasswordCipher)

Este documento descreve o servico de criptografia usado para proteger e recuperar senhas ou valores sensiveis no backend.

## Objetivo
Permitir criptografar e descriptografar strings utilizando uma chave secreta armazenada no `.env`.

## Implementacao
Arquivo:
- `backend/app/services/crypto_service.py`

Classe:
- `PasswordCipher`

Biblioteca usada:
- `cryptography` (Fernet)

## Como funciona
O servico usa a chave `CRYPTO_KEY` carregada a partir do `.env` (via `backend/app/core/config.py`).

- `encrypt`: recebe uma string e retorna um token criptografado.
- `decrypt`: recebe o token criptografado e retorna a string original.

Se a chave for invalida ou o token estiver corrompido, o metodo `decrypt` levanta erro.

## Variaveis de ambiente
No arquivo `.env`:
```
CRYPTO_KEY="meumundo"
```

Observacao: o Fernet exige uma chave no formato base64. Se a chave nao estiver no formato correto, o servico pode falhar ao iniciar. 

## Metodos
### 1) encrypt(password: str) -> str
Criptografa uma string e retorna o token.

Exemplo:
```python
from app.services.crypto_service import PasswordCipher

cipher = PasswordCipher()
secret = cipher.encrypt("minha_senha")
```

### 2) decrypt(token: str) -> str
Descriptografa o token e retorna a string original.

Exemplo:
```python
from app.services.crypto_service import PasswordCipher

cipher = PasswordCipher()
plain = cipher.decrypt(secret)
```

## Erros comuns
- `ValueError: CRYPTO_KEY nao definido`: a variavel nao foi configurada no `.env`.
- `ValueError: Token invalido ou chave incorreta`: chave invalida ou token foi alterado.

## Observacoes finais
- Este servico nao faz hash, ele faz criptografia reversivel.
- Use quando for necessario recuperar o valor original.
- Para senhas de usuarios, prefira hash (ex: bcrypt) em vez de criptografia reversivel.
