import logoMundinho from './assets/logo-mundinho.png'
import './App.css'

function App() {
  return (
    <div className="page">
      <header className="hero">
        <div className="hero-content">
          <div className="brand">
            <img
              className="brand-icon"
              src={logoMundinho}
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
          </form>
        </section>

        <section className="card signup-card">
          <h2>Criar conta</h2>
          <p>Comece agora sua jornada com o Meu Mundinho Feliz.</p>
          <form>
            <label>
              Nome completo
              <input type="text" placeholder="Ana Maria" />
            </label>
            <label>
              E-mail
              <input type="email" placeholder="ana@email.com" />
            </label>
            <label>
              Senha
              <input type="password" placeholder="Crie uma senha" />
            </label>
            <button type="button" className="outline">Criar conta</button>
            <p className="hint">Ao criar sua conta, voce concorda com nossos termos de uso.</p>
          </form>
        </section>
      </main>

      <footer className="footer">
        <p>Meu Mundinho Feliz • Cuidado e conhecimento para a comunidade TEA</p>
      </footer>
    </div>
  )
}

export default App
