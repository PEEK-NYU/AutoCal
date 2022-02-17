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
    return curr_connections[eid] == uid

def create_connection(eid, uid):
    """
    A function that creates a new connection
    """
    dbc.insert_doc(GET_CONNECTS, {eid: uid})
