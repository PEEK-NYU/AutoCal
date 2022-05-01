#!/bin/bash

HOST=127.0.0.1
PORT=8000

export AUTOCAL_DB_PASS=autocall000
export AUTOCAL_DIR=/home/kali/Desktop/AutoCal

if [ $ANUBIS ]
then
    HOST=0.0.0.0
fi

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=API.endpoints flask run --host=$HOST --port=$PORT
