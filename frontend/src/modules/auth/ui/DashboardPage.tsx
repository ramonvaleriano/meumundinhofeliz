import { Link } from 'react-router-dom'

export function DashboardPage() {
  return (
    <div className="page">
      <header className="hero">
        <div className="hero-content">
          <div className="brand">
            <img
              className="brand-icon"
              src={'/src/assets/logo-mundinho.png'}
              alt="Logo do ConectVida"
            />
            <div>
              <p className="brand-tag">Area interna</p>
              <h1>Painel do ConectVida</h1>
            </div>
          </div>
          <p className="hero-text">
            Esta pagina sera desenhada depois. Aqui vamos colocar o painel interno do usuario logado.
          </p>
        </div>
      </header>

      <main className="main">
        <section className="card">
          <h2>Em breve</h2>
          <p>Estamos preparando este painel.</p>
          <Link className="button outline" to="/">Voltar ao login</Link>
        </section>
      </main>
    </div>
  )
}
