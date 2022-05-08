import React, {useState} from 'react';
import axios from 'axios';
import {useTokenContext} from '../../components/TokenContext/TokenContext';
import {useHistory} from 'react-router-dom';

import {backendurl} from '../../config';

import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton';
import EventItem from '../../components/EventItem/EventItem';

export default function Import(){

  const [event_inserted, setInserted] = useState(undefined);
  const {token, setToken} = useTokenContext(); //token, setToken

  return (
    <div className=''>
      <PageTitle text="Import" />
      <input type="file" accept=".ics" onChange={(e)=>{
        const file = e.target.files[0];
        // console.log(await file.text()); //need "async" right before (e)
        if (file) {
            const reader = new FileReader();
            reader.readAsText(file, "UTF-8");
            reader.onload = function (evt) {
                //console.log(evt.target.result);
                axios.post(`${backendurl}/users/calendar/${token}/${evt.target.result}`)
                .then((response) => {
                  //setInserted(response.data); //inserted should be {eventname:x, start_time:00 ...}
                  console.log(Object.values(response.data));
                })
                .catch(error => {
                  console.log(error);
                });
            }
            reader.onerror = function (evt) {
              console.log("error reading file");
            }
        }
      }}></input>
      {event_inserted && (
        <EventItem
          name={event_inserted.eventname}
          start_time={event_inserted.start_time}
          end_time={event_inserted.end_time}
          location={event_inserted.location}
        />
      )}
      <div>
        <NavButton text={'Go Back Home'} subpath={'/'}/>
      </div>
    </div>
  );
};