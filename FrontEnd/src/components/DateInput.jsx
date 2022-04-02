import React from 'react';
import {useState} from 'react';


export default function DateInput({label}){

	const [date, setDate] = useState("2022-01-01");
	const [time, setTime] = useState("00:00");

	return (
	    <div class="sub-main">
			<label for={label}>{label}</label>
			<input 
				type="date" 
			    value={date}
			    min="2022-01-01" 
			    max="2030-12-31"
			    onChange={(e1) => setDate(e1.target.value)}
			    required
			/>
			<input
				type="time" 
				value={time}
			    min="00:00" 
			    max="11:59"
			    onChange={(e2) => setTime(e2.target.value)}
				required
			/>
	    </div>
	)

}