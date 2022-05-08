import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {useTokenContext} from '../../components/TokenContext/TokenContext';
import {useHistory} from 'react-router-dom';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'
import Inputbox from '../../components/Inputbox/Inputbox'


import { backendurl } from '../../config';


const fields = ['Event Name','Start Time','End Time', 'Description'];

export default function Add(){

  const history = useHistory();
  const {token, setToken} = useTokenContext(); //token, setToken
  const [endurl, setEndurl] = useState(`${backendurl}/events/create/${token}`);
  // const [fields,setFields] = useState({});

  // useEffect(() => {
  //   axios.get(`${backendurl}/events/getfields`)
  //     .then((response) => {
  //       setFields(response.data);
  //       console.log(response.data);
  //     })
  //     .catch(error => {
  //       console.log(error);
  //     });
  // }, [])

  const handleAdd = (e) => { 
    e.preventDefault();
    setEndurl( endurl +
      Object.values(e.target.efield).map((field_content, index) => {
        return `/${field_content.value}`
      }).join("")
    ); //didn't join the string right away, async maybe?
    console.log(endurl);
    axios.post(endurl)
      .then((response) => {
        console.log(response.data);
        history.push('/'); //navigate to home
      })
      .catch(error => {
        console.log(error);
      })
  }


  return (
    <div className="content">
      <div className="event-header">
        <PageTitle
          text="Event"
        />
      </div>

      <form onSubmit={handleAdd}>
        {fields ? fields.map((field, index) => (
          <div key={index}>
            <input type="text" name="efield" placeholder={field}/>
          </div>
        )) : (
          <Inputbox
            label={''}
            placeholder={'NO FIELDS FOUND, BACKEND ERROR'}
          />
        )}
        {fields && (
          <div>
            <button type="submit">Add Event</button>
          </div>
        )}

      </form>

      <div className="Edit Event">
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>
    </div>
  );
};