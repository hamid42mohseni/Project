import React from 'react'



const Header = () => {
    fetch("http://127.0.0.1:8000/users/Users/")
    .then(response => response.json())
    .then(json=> console.log(json))
  return (
    <div>
        <h1>Header Component!</h1>
    </div>
  )
}

export default Header
