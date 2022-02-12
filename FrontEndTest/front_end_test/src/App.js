import React from 'react'; //always required
import {useState} from 'react'; //for setting values
import {useEffect} from 'react'; //for fetching data?
import Room from './Room'; //for React Component

export default function App(){
  const [counter, setCounter] = useState(0); // A State Variable
  // const [Var, update_func] = useState(def_val_Var);
  // Var, function exposed to set the Var, default val for Var
  // update_func_name is just an alias for the function, like import random as rd
  // Cor: <button onClick={incCounter}>

  const [aString, setAString] = useState('');
  // Cor: <button onClick={()=> addText(norm_val)}> 

  let norm_val = 'react';


  function incCounter(){
    setCounter(counter + 1);
  }

  function addText(val){
    setAString(aString + val);
  }

//==========================================================

  const [rooms, setRooms] = useState(undefined);

  //npm install axios
  //invoked when element gets rendered, like init
  //the '' should be the url for the endpoint
  useEffect(()=>{
    axios.get('')
      .then((res)=>{
        console.log(res); //res is the object returned by server, data is a key of the res object
        if (res.data){
          setRooms(res.data);
        }

      }); //will only be executed when the above statement returns, in this case the data from the server
  }, []) //[] is the dependency array, MUST pass it, now the funciton only gets called when mounts or rerenders
  
  


  return (
    <div>

      <button onClick={incCounter}> {/*NO (), Important, only runs when clicked*/}
        inc Counter
      </button>
      
      <button onClick={()=> addText(norm_val)}> {/* passing parameters */}
        add text
      </button>


    {/*An React Component, Defined Elsewhere, see import*/}
      <div>
        <Room roomName={"Room A"} numUsers={3}/>
      </div>

      <div>
        {/*Conditionally rendered, only renders when rooms!=undefined*/}
        {rooms &&
          <div>
            {rooms[0].roomName}
          </div>
        }
      </div>
      


    </div>

  )

}