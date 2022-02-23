import React from 'react'; //always required

import {useState} from 'react'; //for setting values
import {useEffect} from 'react'; //for fetching data?

import Room from './Room'; //for React Component



export default function App(){

//==========================================================


  //Part 1 related

  const [counter, setCounter] = useState(0); // A State Variable
  // const [Var, update_func] = useState(default_Var);
  // Var, function exposed to set the Var, default val for Var
  // update_func is just an alias for the function, like rd for import random as rd
  // Cor: <button onClick={incCounter}>

  const [aString, setAString] = useState('');
  // Cor: <button onClick={()=> addText(norm_val)}> 

  let norm_val = 'react';         // a normal variable and a value


  //defining functions
  function incCounter(){
    setCounter(counter + 1);
  }

  function addText(val){
    setAString(aString + val);
  }


//==========================================================


//Part 2 related
  const [rooms, setRooms] = useState(undefined);
  const [error, setError] = useState('');
  const [showRooms, setShowRooms] = useState(true);

  //npm install axios
  //invoked when element gets rendered, like init
  //TODO: the '' should be the url for the endpoint
  useEffect(()=>{
    axios.get(``)                 //a get request
      .then((res)=>{              //only executes after receiving returned data from server
        console.log(res); 
        if (res.data){            //res is the object returned by server, data is a key of the res object
          setRooms(res.data);
        }
      })
      .catch((err)=>{             //error handling
        console.log(err.toString());
        setError(err);
      })
  }, [refresh]) 
  //[] is the dependency array, MUST pass it, now the funciton only gets called when mounts or rerenders
  //PART3 related portion: [] -> [refresh], now the function will also get called when var refresh changes 


//==========================================================


//Part 3 related
  //a function that returns an html component and does nothing else
  const Title = ()_=> (
    <h1> hello </h1>
  )

  const [newRoomName, setNewRoomName] = useState('');
  const [refresh, setRefresh] = useState(0);
  
  const handleCreateRoom = () => {
    axios.post(`${newRoomName}`)  //post request with parameter
      .then((res)=>{
        console.log(res);
        setRefresh(refresh + 1); //keeps adding, then how to reset??
      })
      .catch((err)=>{
        console.log(err);
        setError(err.toString());
      })
  }

//==========================================================


  return (
    <div>
    {/*===============================================================================*/}

      {/*Part 1 related*/}
      <button onClick={incCounter}> {/*Important: NO () after function name! only runs when clicked*/}
        inc Counter
      </button>
      
      <button onClick={()=> addText(norm_val)}> {/* similar to above, but with parameters passed */}
        add text
      </button>

    {/*An React Component, defined in another file, see import*/}
      <div>
        <Room roomName={"Room A"} numUsers={3}/> {/*roomName, numUsers are variables defined by the correlated .jsx file, not related to backend stuff*/}
      </div>

    {/*===============================================================================*/}
    {/*Part 2 related*/}
      <button onClick={()=>setShowRooms(!showRooms)}> {/*just show how the conditional components works*/}
        toggle show rooms
      </button>

      <div>
        {/*Conditionally rendered, only renders when rooms!=undefined && showRooms == True*/}
        {/*Make sure when you render data, data is defined*/}
        {rooms && showRooms &&
          <div>
            {rooms[0].roomName} {/*roomName is related to backend stuff (I THINK! PLZ DOUBLE CHECK!)*/}
          </div>
        }
        {error} {/*empty str by default, so it will only appear when an error occurs*/}
      </div>

    {/*.map iterates through rooms, rooms[index]=room*/}
      <div>
        {rooms && rooms.map((room, index) => (
          <Room
            key = {`${room.roomName}-${index}`} {/*javascript composing strings*/}
            roomName = {room.roomName}
            numUsers = {room.num_users}
          />
        ))}

{/*===============================================================================*/}
    {/*Part 3 related :: TODO add more buttons that invoke certain fields */}
        <input 
          value={newRoomName}
          onChange={(event)=>setNewRoomName(event.target.value)}
          placeholder={'New Room Name'}
        />
        <button onClick={handleCreateRoom}> Create new room </button>
      </div>
    </div>

  )

}