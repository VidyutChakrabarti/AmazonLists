import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Productform from './pages/Productform'
import Home from './pages/Landing'

const App = () => {
  return (
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path='/ListProduct' element={<Productform />} />
    </Routes>
  )
}

export default App
