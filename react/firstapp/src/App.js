import React from 'react';

import './style.css';

function App(){
  return <div>
    <nav className="nav">
      <div className='name'>Wai Linn Kyaw</div>
      <div className='navbar'>
        <div><a className='nav-link' href="">HOME</a></div>
        <div><a className='nav-link' href="">ABOUT</a></div>
        <div><a className='nav-link' href="">SERVICES</a></div>
        <div><a className='nav-link' href="">PROJECTS</a></div>
        <div><a className='nav-link' href="">CONTACT</a></div>
      </div>
    </nav>
    <div className='home'>
      <h1 align="center">Welcome to my Portfolio Site.</h1>
    </div>
  </div>
}

export default App;