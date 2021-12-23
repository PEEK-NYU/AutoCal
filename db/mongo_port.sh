#!/bin/bash

export passwd=$MONGO_PASSWD
export db="peekDB"
export collect="users"
export key="userName"

python3 mongo_port.py $db $collect $key $passwd

export collect="events"
export key="_id"

python3 mongo_port.py $db $collect $key $passwd

export collect="breaks"
export key="_id"

python3 mongo_port.py $db $collect $key $passwd
