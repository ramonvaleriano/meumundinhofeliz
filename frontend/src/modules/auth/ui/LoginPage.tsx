import { Link } from 'react-router-dom'

export function LoginPage() {
  return (
    <div className="page">
      <header className="hero">
        <div className="hero-content">
          <div className="brand">
            <img
              className="brand-icon"
              src={"/src/assets/logo-mundinho.png"}
              alt="Logo do Meu Mundinho Feliz"
            />
            <div>
              <p className="brand-tag">Comunidade, cuidado e conhecimento</p>
              <h1>Meu Mundinho Feliz</h1>
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
              <input type="email" placeholder="voce@email.com" />
            </label>
            <label>
              Senha
              <input type="password" placeholder="********" />
            </label>
            <button type="button">Entrar</button>
            <a className="link" href="#">Esqueci minha senha</a>
            <Link className="button outline" to="/criar-conta">Criar conta</Link>
          </form>
        </section>
      </main>

      <footer className="footer">
        <p>Meu Mundinho Feliz • Cuidado e conhecimento para a comunidade TEA</p>
      </footer>
    </div>
  )
}
