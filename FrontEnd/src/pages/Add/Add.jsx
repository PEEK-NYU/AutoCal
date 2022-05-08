import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {useTokenContext} from '../../components/TokenContext/TokenContext';
import {useHistory} from 'react-router-dom';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton'
import Inputbox from '../../components/Inputbox/Inputbox'


import { backendurl } from '../../config';
import './add.css';



export default function Add(){

  const history = useHistory();
  const {token, setToken} = useTokenContext(); //token, setToken
  const [fields, setFields] = useState(undefined);

  const create_url = `${backendurl}/events/create/${token}`;

  useEffect(() => {
    axios.get(`${backendurl}/events/get_fields`)
      .then((response) => {
        setFields(response.data);
        //console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, [])

  const handleAdd = (e) => { 
    e.preventDefault();
    let endurl = create_url + 
            Object.values(e.target.efield).map((field_content, index) => {
              return `/${field_content.value}`
            }).join("");
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
    <div className="Add">
      <div className="event-header">
        <PageTitle
          text="Event"
        />
      </div>

      <form onSubmit={handleAdd}>
        {fields ? fields.map((field, index) => (
          <div key={index} className="inputbox">
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