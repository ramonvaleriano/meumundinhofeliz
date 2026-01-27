import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { env } from '@/shared/services/env'

export function LoginPage() {
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  const handleLogin = async () => {
    setError(null)
    setLoading(true)
    console.info('Login: iniciando autenticacao')

    try {
      const response = await fetch(`${env.apiBaseUrl}/api/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      })

      if (!response.ok) {
        const detail = await response.text()
        console.error('Login: erro ao autenticar', detail)
        throw new Error(detail)
      }

      const data = await response.json()
      console.info('Login: sucesso', data)
      navigate('/painel')
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Erro inesperado'
      console.error('Login: erro no fluxo', message)
      setError(message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <header className="hero">
        <div className="hero-content">
          <div className="brand">
            <img
              className="brand-icon"
              src={"/src/assets/logo-mundinho.png"}
              alt="Logo do ConectVida"
            />
            <div>
              <p className="brand-tag">Comunidade, cuidado e conhecimento</p>
              <h1>ConectVida</h1>
            </div>
          </div>
          <p className="hero-text">
            Um espaco acolhedor para familias e profissionais que convivem com o autismo. Aqui voce encontra
            formularios, estudos e ferramentas de apoio.
          </p>
          <div className="color-ribbon" aria-hidden="true">
            <span />
            <span />
            <span />
            <span />
          </div>
        </div>
      </header>

      <main className="main">
        <section className="card login-card">
          <h2>Entrar</h2>
          <p>Acesse sua conta para acompanhar formularios e relatorios.</p>
          <form>
            <label>
              E-mail
              <input
                type="email"
                placeholder="voce@email.com"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
            </label>
            <label>
              Senha
              <input
                type="password"
                placeholder="********"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </label>
            <button type="button" onClick={handleLogin} disabled={loading}>
              {loading ? 'Entrando...' : 'Entrar'}
            </button>
            <a className="link" href="#">Esqueci minha senha</a>
            <Link className="button outline" to="/criar-conta">Criar conta</Link>
          </form>
          {error ? <p className="error-banner">{error}</p> : null}
        </section>
      </main>

      <footer className="footer">
        <p>ConectVida • Cuidado e conhecimento para a comunidade TEA</p>
      </footer>
    </div>
  )
}
