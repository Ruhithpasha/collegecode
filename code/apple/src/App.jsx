import React from 'react'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Highlights from './components/Highlights'
import Footer from './components/Footer'
const App = () => {
  return (
    <div>
     <main className='bg-black'>
      <Navbar />
      <Hero />
      <Highlights />
      <Footer />
     </main>
    </div>
  )
}

export default App
