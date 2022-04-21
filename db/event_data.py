"""
This file will manage interactions with the events and event data

Sample of Event Architecture for Refrence:
{
  "events":
  {
    "_id": {
      "eventname": "study session 1",
      "start_time": "datetime?",
      "end_time": "datetime?",
      "location": "home",
      "description": "do design project homework..."
    }
  }
}
"""

import os
import db.db_connect as dbc
import db.connect_data as cdata

# ref in other _data.py files
OK = 0
NOT_FOUND = 1
DUPLICATE = 2

AUTOCAL_HOME = os.environ["AUTOCAL_DIR"]
GET_EVENTS = "events"
EVENTS = "_id"
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
    ret = dbc.fetch_all(GET_EVENTS, EVENTS)
    final_dict = {}
    for event_info in ret:
        new_key = event_info[EVENTS]['$oid']
        final_dict[new_key] = {ENAME: event_info[ENAME],
                               STIME: event_info[STIME],
                               ETIME: event_info[ETIME],
                               LOC: event_info[LOC],
                               DESC: event_info[DESC]}
    # print("fetched events:", final_dict, "\n")
    # print("unformatted:", ret)
    return final_dict


def generate_eid():
    """
    A function that generates a random _event_id key
    TODO: replace with mongo method
    Possibly Helpful:
    'If a document arrives to the database without 
    an _id value, then the database itself will 
    assign an ObjectID to the _id field.'
    
    And to generate a new ObjectID we can do:
    x = ObjectId()
    
    In this example, the value of x would be some:
    ObjectId("507f1f77bcf86cd799439011")
    """
    return "eid_placeholder"


def get_user_events(uid):
    """
    A function that returns a hashmap of events connected to a given uid
    """
    curr_events = get_all_events()
    connected_events = {}
    for eid, event_info in curr_events.items():
        if cdata.is_connected(eid, uid):  # connection_data.py
            connected_events[eid] = event_info
    # if len(connected_events) == 0: return NOT_FOUND
    return connected_events


def find_event(uid, keyword):
    """
    A function to return a list of events under a uid with an eventname keyword
    """
    users_events = get_user_events(uid)
    event_list = {}
    for eid, event_info in users_events.items():
        if keyword in event_info[ENAME]:
            event_list[eid] = event_info
    return event_list


def get_event(eid):
    """
    A function that returns all event information for a given event (eid)
    """
    return get_all_events()[eid]


def create_event(uid, event_name, start_time, end_time,
                 location="", description=""):
    """
    A function that creates an event
    """
    # TODO: check user exists without creating partial init error
    event_info = {ENAME: event_name, STIME: start_time, ETIME: end_time,
                  LOC: location, DESC: description}
    ret = dbc.insert_doc(EVENTS, event_info)
    cdata.create_connection(str(ret.inserted_id), uid)
    return str(ret.inserted_id)


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
