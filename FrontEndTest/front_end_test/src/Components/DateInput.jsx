import React from 'react';
import {useEffect} from 'react';


export default function DateInput({label}){

	return (
	    <div class="sub-main">
			<label for={label}>{label}</label>
			<input type="date" id="start" name="trip-start"
			       value="2018-07-22"
			       min="2018-01-01" max="2018-12-31"/>
			<input type="time" id="appt" name="appt"
			       min="09:00" max="18:00" required/>
	    </div>
	)

}