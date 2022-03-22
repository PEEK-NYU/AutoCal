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

Actual Autocal Architecture example: (TODO; please change - changed?)
{ 
    "_id" : ObjectId("6223ba54024eb2d8c26fc0cc"), 
    "username" : "Elizabeth",
    "password" : "superSecret00",
    "email" : "Beth",
    "calendar" : {
    }
}
"""

import os

import db.db_connect as dbc

import random
import string

import db.connect_data.py as cdata
from user_data import OK, NOT_FOUND, DUPLICATE

DEMO_HOME = os.environ["DEMO_HOME"]
GET_EVENTS = "events"
EVENTS = "_event_id"
ENAME = "eventname"
STIME = "start_time"
ETIME = "end_time"
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
    return dbc.fetch_all_as_dict(GET_EVENTS, EVENTS)


def generate_eid():
    """
    A function that generates a random _user_id key
    """
    # TODO: replace with more reliable method
    curr_events = get_all_events()
    new_eid = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=10))
    if new_eid in curr_events.keys():
        return generate_eid()  # recursively make sure no repeat eid's
    return generate_eid


def get_user_events(uid):
    """
    A function that returns a hashmap of events connected to a given uid
    """
    curr_events = get_all_events()
    connected_events = {}
    for eid, event_info in curr_events.items():
        if cdata.is_connected(eid, uid):  # connection_data.py
            connected_events[eid] = uid
    # if len(connected_events) == 0: return NOT_FOUND
    return connected_events


def find_event(uid, keyword):
    """
    A function to return a list of events under a uid with an eventname keyword
    """
    curr_events = get_user_events(uid)
    event_list = {}
    for eid, event_info in curr_events.items():
        if keyword in event_info[ENAME]:
            event_list[eid] = event_info
    return event_list


def get_event(eid):
    """
    A function that returns all event information for a given event (eid)
    """
    curr_events = get_all_events()
    return curr_events[eid]


def create_event(uid, event_name, start_time, end_time,
                 location="", description=""):
    """
    A function that creates an event
    """
    event_info = {ENAME: event_name, STIME: start_time, ETIME: end_time,
                  LOC: location, DESC: description}
    new_eid = generate_eid()
    dbc.insert_doc(EVENTS, {new_eid: event_info})
    cdata.create_connection(new_eid, uid)  # connect new event to current user
    return OK


def event_exists(eid):
    """
    A function that checks if an event exists
    """
    curr_events = get_all_events()
    if eid in curr_events.keys():
        return OK
    return NOT_FOUND


def del_event(eid, uid):
    """
    A function that deletes an event (and relating connection)
    """
    if event_exists(eid) is NOT_FOUND:
        return NOT_FOUND  # check for event
    assert cdata.is_connected(eid, uid) is OK  # check user connected to event
    dbc.del_one(GET_EVENTS, filters={EVENTS: eid})
    return cdata.del_connection(eid, uid)
