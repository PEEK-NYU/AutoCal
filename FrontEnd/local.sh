#!/bin/sh

# See if something is already running on our port.

export LOCAL_MONGO=0   # we could make this a parameter!

export API_PORT=8000
export AUTOCAL_DB_PASS=autocal000
export AUTOCAL_DIR=/home/kali/Desktop/AutoCal


# look for a process running on $PORT:
export server=$(ps -ef | grep "[p]ort=$API_PORT")
echo "Server = $server"
if [ -z "$server" ]
then
    # run local server in the background:
    echo "No running Chat API server detected: launching."
    cd $AUTOCAL_DIR && ./local.sh &
else
    echo "A server is already running on port $API_PORT"
fi

export REACT_APP_BACKEND_URL=http://127.0.0.1:$API_PORT/


#npm install
#npm install @fullcalendar/react @fullcalendar/daygrid
npm run start
echo "If you need to kill the API Server, you can run the ps command and kill its PID."

