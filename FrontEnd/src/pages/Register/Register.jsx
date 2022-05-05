import React, {useState} from 'react';
import axios from 'axios';
import {useTokenContext} from '../../components/TokenContext/TokenContext';
import {useHistory} from 'react-router-dom';

import {backendurl} from '../../config';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton';


export default function Register(){

  const history = useHistory();
  const [username, setUserName] = useState('');
  const [password, setPassword] = useState('');  
  const [email, setEmail] = useState('');  
  const [error, setError] = useState(undefined);
  const {token, setToken} = useTokenContext(); //token, setToken

  const handleRegister = (e) => { 
    e.preventDefault();
    axios.post(`${backendurl}/users/create/${username}/${password}/${email}`)
      .then((response) => {
        console.log(response.data);
        setToken(response.data); //set token to user id
        history.push('/'); //navigate to home
      })
      .catch(error => {
        console.log(error);
        setError(error);
      })
  }

  return (
    <div className="content">
      <div className="register-header">
        <PageTitle
          text="Register"
        />
      </div>

      {error && (
          <div className="register-error-box">
            <p>{error.toString()}</p>
          </div>
      )}

      <div className="register-form">
        <form onSubmit={e=>{e.preventDefault()}}>
          <label>
            <p>Username</p>
            <input type="text" onChange={e => setUserName(e.target.value)}/>
          </label>
          <label>
            <p>Password</p>
            <input type="password" onChange={e => setPassword(e.target.value)}/>
          </label>
          <label>
            <p>Email</p>
            <input type="text" onChange={e => setEmail(e.target.value)}/>
          </label>
          <div>
            <button type="submit" onClick={handleRegister}>Submit</button>
          </div>
        </form>
      </div>

      <NavButton text={'Go Back Home'} subpath={'/'}/>

    </div>
  );
};
