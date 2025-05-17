import React from 'react'
import { appleImg,bagImg,searchImg } from '../utils'
import {navLists} from '../constants'
const Navbar = () => {
  return (
    <div>
      <header className='w-full py-5 sm:px-10 px-5 flex justify-between items-center'>
        <nav className='flex w-full screen-max-width'>
          <img src={appleImg} alt="Apple" height={18} width={14} />

          <div className='flex flex-1 justify-center max-sm:hidden'>
            {navLists.map((nav) => (
              <div key={nav} className="px-5 text-gray-500 hover:text-white cursor-pointer transition-all">
                {nav}
              </div>
            ))}
          </div>
          <div className='flex items-baseline gap-7 max-sm:justify-end max-sm:flex-1'>
            <img src={searchImg} alt="search img" height={18} width={18} />
            <img src={bagImg} alt="Bag image" width={18} height={18} />
          </div>
        </nav> 
      </header>
    </div>
  )
}

export default Navbar
