import React, {useEffect, useState, useContext} from 'react';
import FullCalendar from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin

import NavButton from '../../components/NavButton/NavButton';
import { useTokenContext } from '../../components/TokenContext/TokenContext';

export default function Home(){

  const {token, setToken, dummy, setDummy} = useTokenContext(); //token, setToken
  // const context = useTokenContext(); //context.token, context.setToken

  return (
    <div className="content">
      <h1>AutoCal</h1>
      <p> CALENDER PLANNER FOR ALL </p>
      <div>
        {token ? 
            <button onClick={() => setToken(null)}>
              Logout
            </button>
        : (
            <NavButton text={'Login/Register'} subpath={'/logreg'}/>
        )}
      </div>
      <FullCalendar
        plugins={[ dayGridPlugin ]}
        initialView="dayGridMonth"
        aspectRatio={2}
        height={500}
      />
    </div>
  );
};

