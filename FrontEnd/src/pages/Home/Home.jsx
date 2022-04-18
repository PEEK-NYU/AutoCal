import React, {useEffect, useState} from 'react';
import FullCalendar from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin

import NavButton from '../../components/NavButton/NavButton';

export default function Home(){

  const [isLoggedIn, setisLoggedIn] = useState(true); //set to true for testing, should be false

  return (
    <div className="content">
      <h1>AutoCal</h1>
      <p> CALENDER PLANNER FOR ALL </p>
      <div>
        {isLoggedIn ? 
            <button onClick={() => setisLoggedIn(false)}>
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

