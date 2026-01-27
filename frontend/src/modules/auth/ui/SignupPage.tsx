import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { env } from '@/shared/services/env'

type ProfileType = {
  id: number
  user_type: string
}

type FeatureFlag = {
  id: number
  name_flag: string
}

export function SignupPage() {
  const navigate = useNavigate()
  const [profileTypes, setProfileTypes] = useState<ProfileType[]>([])
  const [selectedProfileType, setSelectedProfileType] = useState<ProfileType | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  const [form, setForm] = useState({
    name: '',
    surname: '',
    birth_date: '',
    cpf: '',
    cellphone: '',
    email: '',
    password: '',
    cep: '',
    tipo_logradouro: '',
    logradouro: '',
    bairro: '',
    estado: '',
    numero: '',
    complemento: '',
    referencia: '',
  })

  useEffect(() => {
    const loadProfileTypes = async () => {
      try {
        const response = await fetch(`${env.apiBaseUrl}/api/profile-types/all`)
        if (!response.ok) return
        const data = (await response.json()) as ProfileType[]
        setProfileTypes(data)
      } catch {
        setProfileTypes([])
      }
    }

    loadProfileTypes()
  }, [])

  const updateField = (key: keyof typeof form, value: string) => {
    setForm((prev) => ({ ...prev, [key]: value }))
  }

  const handleSubmit = async () => {
    setError(null)
    if (!selectedProfileType) {
      console.error('Cadastro: tipo de perfil nao selecionado')
      setError('Selecione um tipo de perfil.')
      return
    }

    setLoading(true)
    try {
      console.info('Cadastro: iniciando criacao de endereco')
      const addressResponse = await fetch(`${env.apiBaseUrl}/api/addresses/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          cep: form.cep,
          estado: form.estado,
          bairro: form.bairro,
          tipo_logradouro: form.tipo_logradouro,
          logradouro: form.logradouro,
          numero: form.numero,
          complemento: form.complemento || null,
          referencia: form.referencia || null,
        }),
      })

      if (!addressResponse.ok) {
        const detail = await addressResponse.text()
        console.error('Cadastro: erro ao criar endereco', detail)
        throw new Error(`Erro ao criar endereco: ${detail}`)
      }

      const addressData = await addressResponse.json()
      console.info('Cadastro: endereco criado', addressData)

      console.info('Cadastro: buscando feature flags')
      const featureResponse = await fetch(
        `${env.apiBaseUrl}/api/feature-flags/?skip=0&limit=100`
      )

      if (!featureResponse.ok) {
        const detail = await featureResponse.text()
        console.error('Cadastro: erro ao buscar feature flags', detail)
        throw new Error(`Erro ao buscar feature flags: ${detail}`)
      }

      const featureFlags = (await featureResponse.json()) as FeatureFlag[]
      const isResponsible =
        selectedProfileType.user_type === 'País' ||
        selectedProfileType.user_type === 'Responsável Legal'
      const expectedFlag = isResponsible ? 'average_user' : 'professional_tools'
      const selectedFlag = featureFlags.find((item) => item.name_flag === expectedFlag)

      if (!selectedFlag) {
        console.error('Cadastro: feature flag nao encontrada', expectedFlag)
        throw new Error(`Feature flag nao encontrada: ${expectedFlag}`)
      }

      console.info('Cadastro: criando usuario')
      const userResponse = await fetch(`${env.apiBaseUrl}/api/users/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: form.name,
          surname: form.surname,
          email: form.email,
          cpf: form.cpf,
          cellphone: form.cellphone,
          birth_date: form.birth_date,
          password: form.password,
          address: addressData.id,
          is_active: true,
          is_verified: true,
          role: [selectedFlag.id],
          last_login: new Date().toISOString(),
        }),
      })

      if (!userResponse.ok) {
        const detail = await userResponse.text()
        console.error('Cadastro: erro ao criar usuario', detail)
        throw new Error(`Erro ao criar usuario: ${detail}`)
      }

      console.info('Cadastro: usuario criado com sucesso')
      navigate('/painel')
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Erro inesperado'
      console.error('Cadastro: erro no fluxo', message)
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
              src={'/src/assets/logo-mundinho.png'}
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
              <input
                type="text"
                placeholder="Ana"
                value={form.name}
                onChange={(event) => updateField('name', event.target.value)}
              />
            </label>
            <label>
              Sobrenome
              <input
                type="text"
                placeholder="Silva"
                value={form.surname}
                onChange={(event) => updateField('surname', event.target.value)}
              />
            </label>
            <label>
              Data de nascimento
              <input
                type="date"
                value={form.birth_date}
                onChange={(event) => updateField('birth_date', event.target.value)}
              />
            </label>
            <label>
              CPF
              <input
                type="text"
                placeholder="123.456.789-00"
                value={form.cpf}
                onChange={(event) => updateField('cpf', event.target.value)}
              />
            </label>
            <label>
              Celular
              <input
                type="tel"
                placeholder="(11) 99999-9999"
                value={form.cellphone}
                onChange={(event) => updateField('cellphone', event.target.value)}
              />
            </label>
            <label className="full">
              E-mail
              <input
                type="email"
                placeholder="ana@email.com"
                value={form.email}
                onChange={(event) => updateField('email', event.target.value)}
              />
            </label>
            <label className="full">
              Senha
              <input
                type="password"
                placeholder="Crie uma senha"
                value={form.password}
                onChange={(event) => updateField('password', event.target.value)}
              />
            </label>
            <label className="full">
              Tipo de Perfil
              <select
                value={selectedProfileType?.id ?? ''}
                onChange={(event) => {
                  const id = Number(event.target.value)
                  const found = profileTypes.find((item) => item.id === id) ?? null
                  setSelectedProfileType(found)
                }}
              >
                <option value="">Selecione</option>
                {profileTypes.map((item) => (
                  <option key={item.id} value={item.id}>
                    {item.user_type}
                  </option>
                ))}
              </select>
            </label>
          </form>
        </section>

        <section className="card signup-card">
          <h2>Endereco</h2>
          <form className="form-grid">
            <label>
              CEP
              <input
                type="text"
                placeholder="01000-000"
                value={form.cep}
                onChange={(event) => updateField('cep', event.target.value)}
              />
            </label>
            <label>
              Tipo de logradouro
              <select
                value={form.tipo_logradouro}
                onChange={(event) => updateField('tipo_logradouro', event.target.value)}
              >
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
              <input
                type="text"
                placeholder="Rua das Flores"
                value={form.logradouro}
                onChange={(event) => updateField('logradouro', event.target.value)}
              />
            </label>
            <label>
              Bairro
              <input
                type="text"
                placeholder="Centro"
                value={form.bairro}
                onChange={(event) => updateField('bairro', event.target.value)}
              />
            </label>
            <label>
              Estado
              <input
                type="text"
                placeholder="SP"
                value={form.estado}
                onChange={(event) => updateField('estado', event.target.value)}
              />
            </label>
            <label>
              Numero
              <input
                type="text"
                placeholder="123"
                value={form.numero}
                onChange={(event) => updateField('numero', event.target.value)}
              />
            </label>
            <label>
              Complemento
              <input
                type="text"
                placeholder="Apto 101"
                value={form.complemento}
                onChange={(event) => updateField('complemento', event.target.value)}
              />
            </label>
            <label className="full">
              Referencia
              <input
                type="text"
                placeholder="Proximo a praca"
                value={form.referencia}
                onChange={(event) => updateField('referencia', event.target.value)}
              />
            </label>
          </form>
        </section>
      </main>

      {error ? <p className="error-banner">{error}</p> : null}

      <div className="action-bar">
        <Link className="button ghost" to="/">Voltar</Link>
        <button className="button primary" type="button" onClick={handleSubmit} disabled={loading}>
          {loading ? 'Enviando...' : 'Finalizar cadastro'}
        </button>
      </div>

      <footer className="footer">
        <p>Ao criar sua conta, voce concorda com nossos termos de uso.</p>
      </footer>
    </div>
  )
}
