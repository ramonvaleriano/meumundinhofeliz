import { Routes, Route } from 'react-router-dom'
import './App.css'
import { LoginPage } from './modules/auth/ui/LoginPage'
import { SignupPage } from './modules/auth/ui/SignupPage'

function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/criar-conta" element={<SignupPage />} />
    </Routes>
  )
}

export default App
