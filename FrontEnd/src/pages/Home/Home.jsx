import React, {useEffect, useState, useContext} from 'react';
import FullCalendar from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin

import NavButton from '../../components/NavButton/NavButton';
import { useTokenContext } from '../../components/TokenContext/TokenContext';
import './home.css'

export default function Home(){

  const {token, setToken, dummy, setDummy} = useTokenContext(); //token, setToken
  // const context = useTokenContext(); //context.token, context.setToken

  return (
    <div className="Home">
      <h1>AutoCal</h1>
      <p> CALENDER PLANNER FOR ALL </p>
      {token ? 
          <div>
            <div className='Logout'>
              <button onClick={() => setToken(null)}>
                Logout
              </button>
            </div>
            <div className = 'Menu'>   
              <ul className = "NavBar">
                <li><NavButton text={'Account Settings'} subpath={'/account'}/></li>
                <li><NavButton text={'Event Search'} subpath={'/search'}/></li>
                <li><NavButton text={'Add Event'} subpath={'/add'}/></li>
                <li><NavButton text={'Import'} subpath={'/import'}/></li>
              </ul> 
              <div className = 'Calendar'>
                <FullCalendar
                  plugins={[ dayGridPlugin ]}
                  initialView="dayGridMonth"
                  aspectRatio={1.5}
                  height={500}
                />
            </div>
          </div> 
        </div>
      : (
          <div>
            <div className='Header'>
              <NavButton text={'Login'} subpath={'/login'}/>
              <NavButton text={'Register'} subpath={'/register'}/>
            </div>
            <div className = 'Menu'>   
              <ul className = "NavBar">
                <li><NavButton text={'Account Settings'} subpath={'/'}/></li>
                <li><NavButton text={'Event Search'} subpath={'/'}/></li>
                <li><NavButton text={'Add Event'} subpath={'/'}/></li>
                <li><NavButton text={'Import'} subpath={'/'}/></li>
              </ul> 
              <div className = 'Calendar'>
                <FullCalendar
                  plugins={[ dayGridPlugin ]}
                  initialView="dayGridMonth"
                  aspectRatio={1.5}
                  height={500}
                />
              </div>
            </div> 
          </div>
      )}
    </div>
  );
};

