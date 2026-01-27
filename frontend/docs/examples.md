# Exemplos (Desenvolvedor) - Frontend

## Buscar tipos de perfil
```ts
import { env } from '@/shared/services/env'

const res = await fetch(`${env.apiBaseUrl}/api/profile-types/all`)
const data = await res.json()
```

## Estrutura basica de pagina
```tsx
export function MinhaPagina() {
  return (
    <div>
      <h1>Titulo</h1>
      <p>Texto</p>
    </div>
  )
}
```

## Estrutura de formulario
```tsx
<form>
  <label>
    Nome
    <input type="text" />
  </label>
</form>
```
