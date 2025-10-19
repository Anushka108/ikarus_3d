import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'
import './styles.css'
import logo from './assets/ikarus-logo.svg'
import ChatPage from './pages/ChatPage'
import AnalyticsPage from './pages/AnalyticsPage'

function App(){
  return (
    <BrowserRouter>
      <div className="container py-4">
        <nav className="navbar navbar-ikarus mb-4 d-flex justify-content-between align-items-center px-3">
          <Link className="d-flex align-items-center navbar-brand" to="/">
            <img src={logo} alt="Ikarus 3D" className="brand-logo" />
            <span className="h5 mb-0 text-white">Ikarus 3D</span>
          </Link>
          <div>
            <Link className="btn btn-ikarus-outline me-2" to="/">Recommend</Link>
            <Link className="btn btn-ikarus" to="/analytics">Analytics</Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<ChatPage/>} />
          <Route path="/analytics" element={<AnalyticsPage/>} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

createRoot(document.getElementById('root')).render(<App />)
