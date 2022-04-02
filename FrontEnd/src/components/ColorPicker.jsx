import React from 'react';
import {useState} from 'react';

export default function ColorPicker(){

	const [color, setColor] = useState("#fffffe");

	return (
	    <div class="sub-main">
			<input 
				type="color" 
			    value={color}
			    onChange={(e) => setColor(e.target.value)}
			    required
			/>
	    </div>
	)
}