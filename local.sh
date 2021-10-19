#!/bin/bash

HOST=127.0.0.1
PORT=8000
if [ $ANUBIS]  # export "ANUBIS=" in bash to rewrite
then
    HOST=0.0.0.0
fi
flask
# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=API.endpoints flask run --host=$HOST --port=$PORT
