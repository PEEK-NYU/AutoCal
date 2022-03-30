import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

import RoomItem from '../../components/RoomItem/RoomItem';
import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'

import {backendurl} from '../../config';

import './rooms.css';

export default function Rooms() {
  const [rooms, setRooms] = useState(undefined);
  const [error, setError] = useState(undefined);

  const [refresh, setRefresh] = useState(undefined);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newRoomName, setNewRoomName] = useState('');

  const history = useHistory();

  useEffect(() => {
    axios.get(`${backendurl}/rooms/list`)
      .then((response) => {
        console.log(response.data);
        if (response.data){
          setRooms(response.data);
        }
      })
      .catch(error => {
        console.log(error);
        setError(error);
      });
  }, [refresh])

  const handleCreateRoom = () => {
    axios.post(`${backendurl}/rooms/create/${newRoomName}`)
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
            className="room-input"
            placeholder="Room Name"
            value={newRoomName}
            onChange={(e) => setNewRoomName(e.target.value)}
          />
          <div className="create-actions">
            <button className="button" onClick={handleCreateRoom}>Create New Room</button>
            <button className="button" onClick={() => setIsModalOpen(false)}> Cancel </button>
          </div>
        </div>
      }

      <div className="rooms-header">
        <PageTitle
          text="Rooms"
        />
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>

      {error && (
        <div className="rooms-error-box">
          <p>{error.toString()}</p>
        </div>
      )}

      <div className="rooms-list">
        {rooms ? rooms.map((room, index) => (
          <RoomItem
            key={`${room.roomName}-${index}`}
            name={room.roomName}
            userCount={room.num_users}
          />
        )) : (
          <div className="rooms-empty">
            <p>Sorry there are no rooms right now... Come back later </p>
          </div>
        )}
      </div>
      <div>
        <button className="page-button" onClick={() => setIsModalOpen(true)}> Add New Room </button>
      </div>
    </div>
  )
}