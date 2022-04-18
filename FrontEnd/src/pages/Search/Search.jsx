//https://www.emgoto.com/react-search-bar/

import React from 'react';

import EventItem from '../../components/EventItem/EventItem';
import PageTitle from '../../components/PageTitle/PageTitle';
import NavButton from '../../components/NavButton/NavButton';

import './Search.css';

const events = [
  { eventname: 'Meeting1', start_time: '11:00', location: '1' },
  { eventname: 'Meeting2', start_time: '12:00', location: '2' },
  { eventname: 'Gym', start_time: '13:00', location: '3' },
  { eventname: 'Bar', start_time: '14:00', location: '4' },
];

export default function Search() {

  //function for filtering events
  const filterEvents = (events, query) => {
    if (!query) {
        return events;
    }
    return events.filter((event) => {
        const eventname = event.eventname.toLowerCase();
        return eventname.includes(query);
    });
  };
 
  const { search } = window.location;
  const query = new URLSearchParams(search).get('input'); //the input string
  const filteredEvents = filterEvents(events, query); //list of events matching

  return (
    <div className="content">

      <PageTitle text={'Event Search'}/>
      
      <form action="/search" method="get">
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
            key={`${event.evetnname}-${index}`}
            name={event.eventname}
            start_time={event.start_time}
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
