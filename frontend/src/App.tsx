import { Routes, Route } from 'react-router-dom'
import './App.css'
import { LoginPage } from './modules/auth/ui/LoginPage'
import { SignupPage } from './modules/auth/ui/SignupPage'
import { DashboardPage } from './modules/auth/ui/DashboardPage'

function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/criar-conta" element={<SignupPage />} />
      <Route path="/painel" element={<DashboardPage />} />
    </Routes>
  )
}

export default App
