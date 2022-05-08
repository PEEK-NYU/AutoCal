import React from 'react';

import './EventItem.css';

export default function EventItem({name, start_time, end_time, location}) {
  return (
    <div className="event-item">
      <h2> {name} </h2>
      <p> start@ {start_time} </p>
      <p> end@ {end_time} </p>
      <p> location@ {location} </p>
    </div>
  );
}
