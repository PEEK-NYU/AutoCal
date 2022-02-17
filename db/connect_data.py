"""
This file will manage interactions between user and event data,
  aka the connection data table.

Sample of Connection Architecture for Refrence:
{
"event_id_1" : "user_id_1"
}
"""

import os

import db.db_connect as dbc

import random
import string

from event_data import EVENTS
from user_data import USERS, OK, NOT_FOUND, DUPLICATE

DEMO_HOME = os.environ["DEMO_HOME"]
GET_CONNECTS = "events"
# EVENTS
# USERS

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)

def get_all_connections():
    """
    A function to return a hashmap of all user:event connections
    """
    return dbc.fetch_all(GET_CONNECTS)

def is_connected(eid, uid):
    """
    A function to check if an event is connected to a user
    """
    curr_connections = get_all_connections()
    if curr_connections[eid] == uid:
        return OK
    else:
        return NOT_FOUND

def create_connection(eid, uid):
    """
    A function that creates a new connection
    """
    dbc.insert_doc(GET_CONNECTS, {eid: uid})

def del_connection(eid, uid):
    """
    A function that deletes a given event-user connection by id
    """
    dbc.del_one(GET_CONNECTS, filters={eid: uid})
    # return OK

def del_events_by_user(del_uid):
    """
    A function that deletes all events under a user's ownership
    """
    curr_connections = get_all_connections()
    for eid, uid in curr_connections:
        if uid == del_uid:
            del_connection(eid,uid)
    # return OK