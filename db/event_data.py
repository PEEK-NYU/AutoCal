"""
This file will manage interactions with the events and event data

Sample of Event Architecture for Refrence:
{
  "event_id_1": {
    "eventname": "study session 1",
    "start_time": "datetime?",
    "end_time": "datetime?",
    "location": "home",
    "description": "do design project homework..."
  }
}
"""

import os

import db.db_connect as dbc

import random
import string

from connect_data import *
from user_data import OK, NOT_FOUND, DUPLICATE

DEMO_HOME = os.environ["DEMO_HOME"]
GET_EVENTS = "events"
EVENTS = "_event_id"
ENAME = "eventname"
STIME = "start_time"
ETIME =  "end_time"
LOC = "location"
DESC = "description"

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)

def get_all_events():
    """
    A function to return a hashmap of all events.
    """
    return dbc.fetch_all(GET_EVENTS)

def generate_eid():
    """
    A function that generates a random _user_id key
    """
    curr_users = get_all_users()
    # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/2257449
    new_uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    if new_uid in curr_users.keys():
        return generate_uid()  # recursively make sure no repeat eid's
    return new_uid

def get_event(uid):
    """
    A function that returns a
    """
    curr_events = get_all_events()
    connected_events = {}
    for eid, event_info in curr_events.items():
        if is_connected(eid, uid):  # connection_data.py
            connected_events[eid] = uid
    # if len(connected_events) == 0: return NOT_FOUND
    return connected_events

def create_event(uid, event_name, start_time, end_time, location = "", description = ""):
    event_info = {ENAME: event_name, STIME: start_time, ETIME: end_time,
                  LOC: location, DESC: description}
    new_eid = generate_eid()
    dbc.insert_doc(EVENTS, {new_eid: event_info})
    new_connection(new_eid, uid)  # connect new event to current user
    return OK
