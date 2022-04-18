import React from 'react';
import './LogRegForm.css';

export default function LogRegForm(){
  return (
    <div className="logregform">
      <form action="/">
        <div className="input-container">
          <label>Username </label>
          <input type="text" name="uname" required />
        </div>
        <div className="input-container">
          <label>Password </label>
          <input type="password" name="pass" required />
        </div>
        <div className="button-container">
          <input type="submit" value="Log Me In"/> 
        </div>
        <div className="button-container">
          <input type="submit" value="Register"/> 
        </div>
      </form>
    </div>
  )
}