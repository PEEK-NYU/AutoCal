//https://www.emgoto.com/react-search-bar/

import React, {useState, useEffect} from 'react';
import { useTokenContext } from '../../components/TokenContext/TokenContext';

import EventItem from '../../components/EventItem/EventItem';
import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton';

import './Search.css';
import axios from 'axios';
import { backendurl } from '../../config';


export default function Search() {

  const {token, setToken} = useTokenContext(); //token, setToken
  const [query, setQuery] = useState('');
  const [error, setError] = useState('');
  const [events, setEvents] = useState({});

  useEffect(() => {
    axios.get(`${backendurl}/events/get/${token}`)
      .then((response) => {
        setEvents(response.data);
        console.log(Object.values(response.data));
      })
      .catch(error => {
        console.log(error);
        setError(error);
      });
  }, [])

  // prevent ? in URL
  const refresh = (e) => {
    e.preventDefault();
    setQuery(e.currentTarget.input.value)
    //console.log(e.currentTarget.input.value);
  }

  //function for filtering events
  const filterEvents = (events, query) => {

    if (!query) {
        return Object.values(events);
    }
    return Object.values(events).filter((event) => {
        const eventname = event.eventname.toLowerCase();
        return eventname.includes(query);
    });
  };

  const filteredEvents = filterEvents(events, query); //list of events matching

  return (
    <div className="Search">
      <PageTitle text={'Event Search'}/>
      
      <form onSubmit={refresh}>
        <input
            type="text"
            id="header-search"
            placeholder="Enter Event Name"
            name="input"
        />
        <button type="submit">Search</button>
      </form>

      <div className="event-list">
        {filteredEvents ? filteredEvents.map((event, index) => (
          <EventItem
            key={`${event.eventname}-${index}`}
            name={event.eventname}
            start_time={event.start_time}
            end_time={event.end_time}
            location={event.location}
          />
        )) : (
          <div className="events-empty">
            <p> Didn't find any result </p>
          </div>
        )}
      </div>

      <NavButton text={'Go Back Home'} subpath={'/'}/>
    </div>
  )
}
