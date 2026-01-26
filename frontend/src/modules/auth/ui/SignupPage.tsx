import { Link } from 'react-router-dom'

export function SignupPage() {
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
              <p className="brand-tag">Cadastro inicial</p>
              <h1>Criar conta</h1>
            </div>
          </div>
          <p className="hero-text">
            Preencha seus dados e o endereco para iniciar sua jornada no ConectVida.
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
        <section className="card signup-card">
          <h2>Dados pessoais</h2>
          <form className="form-grid">
            <label>
              Nome
              <input type="text" placeholder="Ana" />
            </label>
            <label>
              Sobrenome
              <input type="text" placeholder="Silva" />
            </label>
            <label>
              Data de nascimento
              <input type="date" />
            </label>
            <label>
              CPF
              <input type="text" placeholder="123.456.789-00" />
            </label>
            <label>
              Celular
              <input type="tel" placeholder="(11) 99999-9999" />
            </label>
            <label className="full">
              E-mail
              <input type="email" placeholder="ana@email.com" />
            </label>
            <label className="full">
              Senha
              <input type="password" placeholder="Crie uma senha" />
            </label>
          </form>
        </section>

        <section className="card signup-card">
          <h2>Endereço</h2>
          <form className="form-grid">
            <label>
              CEP
              <input type="text" placeholder="01000-000" />
            </label>
            <label>
              Tipo de logradouro
              <select>
                <option value="">Selecione</option>
                <option>Rua</option>
                <option>Avenida</option>
                <option>Travessa</option>
                <option>Alameda</option>
                <option>Estrada</option>
              </select>
            </label>
            <label className="full">
              Logradouro
              <input type="text" placeholder="Rua das Flores" />
            </label>
            <label>
              Bairro
              <input type="text" placeholder="Centro" />
            </label>
            <label>
              Estado
              <input type="text" placeholder="SP" />
            </label>
            <label>
              Numero
              <input type="text" placeholder="123" />
            </label>
            <label>
              Complemento
              <input type="text" placeholder="Apto 101" />
            </label>
            <label className="full">
              Referencia
              <input type="text" placeholder="Proximo a praca" />
            </label>
          </form>
        </section>
      </main>

      <div className="action-bar">
        <Link className="button ghost" to="/">Voltar</Link>
        <button className="button primary" type="button">Finalizar cadastro</button>
      </div>

      <footer className="footer">
        <p>Ao criar sua conta, voce concorda com nossos termos de uso.</p>
      </footer>
    </div>
  )
}
