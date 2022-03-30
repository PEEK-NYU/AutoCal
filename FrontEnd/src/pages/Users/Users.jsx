import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';
import {backendurl} from '../../config';

import NavButton from '../../components/NavButton/NavButton'

import './users.css';

export default function Users() {
  const [users, setUsers] = useState(undefined);
  const [error, setError] = useState(undefined);

  const [refresh, setRefresh] = useState(0);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newUserName, setNewUserName] = useState('');

  const history = useHistory();

  useEffect(() => {
    axios.get(`${backendurl}/users/list`)
      .then((response) => {
        if (response.data){
          setUsers(response.data);
        }
      })
      .catch(error => {
        setError(error);
        console.log(error);
      });
  }, [refresh])

  const handleCreateUser = () => {
    axios.post(`${backendurl}/users/create/${newUserName}`)
      .then(() => {
        setIsModalOpen(false);
        setRefresh(refresh + 1);
      })
      .catch(error => {
        setError(error);
        console.log(error);
      })
  }

  return (
    <div className="content">
      {isModalOpen && 
        <div className="create-modal">
          <input
            className="user-input"
            placeholder="User Name"
            value={newUserName}
            onChange={(e) => setNewUserName(e.target.value)}
          />
          <div className="create-actions">
            <button className="button" onClick={handleCreateUser}>Create New User</button>
            <button className="button" onClick={() => setIsModalOpen(false)}> Cancel </button>
          </div>
        </div>
      }
  
      <div className="rooms-header">
        <h1>Users</h1>
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>

      {error && (
        <div className="rooms-error-box">
          <p>{error.toString()}</p>
        </div>
      )}

      <div className="rooms-list">
        {users ? users.map((user, index) => (
          <div 
            className="user-item"
            key={`${user.userName}-${index}`}
          >
            <p>{user.userName}</p>
            <p>{index}</p>
          </div>
        )) : (
          <div className="rooms-empty">
            <p>Sorry there are no rooms right now... Come back later </p>
          </div>
        )}
      </div>

      <div>
        <button className="page-button" onClick={() => setIsModalOpen(true)}> Add New User </button>
      </div>
    </div>
  )
}