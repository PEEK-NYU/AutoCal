import React from 'react';

import './EventItem.css';

export default function EventItem({name, start_time, location}) {
  return (
    <div className="event-item">
      <p> {name} </p>
      <p> {start_time} </p>
      <p> {location} </p>
    </div>
  );
}


