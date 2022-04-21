"""
This file will manage interactions between user and event data,
  aka the connection data table.

Sample of Connection Architecture for Refrence:
{
  "connections":
  { "_id":
    {
      "_event_id" : "623b953e28c7bbc22066b8a9",
      "_user_id" : "6223ba54024eb2d8c26fc0ce"
    }
  }
}
"""

import os
import db.db_connect as dbc
import db.event_data as edata

# ref in other _data.py files
OK = 0
NOT_FOUND = 1
DUPLICATE = 2

AUTOCAL_HOME = os.environ["AUTOCAL_DIR"]
GET_CONNECTS = "connections"
CONNECTIONS = "_id"
CUSER = "UID"
CEVENT = "EID"

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)


def get_all_connections():
    """
    A function to return a hashmap of all user:event connections
    """
    ret = dbc.fetch_all(GET_CONNECTS, CONNECTIONS)
    final_dict = {}
    for connect_info in ret:
        new_key = connect_info[CONNECTIONS]['$oid']
        final_dict[new_key] = {CUSER: connect_info[CUSER],
                               CEVENT: connect_info[CEVENT]}
    # print("fetched users:", final_dict, "\n")
    return final_dict


def create_connection(eid, uid):
    """
    A function that creates a new connection
    """
    dbc.insert_doc(GET_CONNECTS, {CUSER: uid, CEVENT: eid})


def get_connection(eid, uid):
    """ a function that returns the connect id (cid) given (eid, uid) """
    curr_connections = get_all_connections()
    for key, value in curr_connections.items():
        if value[CEVENT] == eid and value[CUSER] == uid:
            return key
    return NOT_FOUND


def is_connected(eid, uid):
    """
    A function to check if an event is connected to a user
    """
    return get_connection(eid, uid) != NOT_FOUND


def get_connection_from_eid(eid):
    """ ADMIN METHOD for getting uid from eid """
    curr_connections = get_all_connections()
    for key, value in curr_connections.items():
        if value[CEVENT] == eid:
            # Note: assumes each event only connected to 1 user
            return value[CUSER]
    return NOT_FOUND


def del_connection(eid, uid):
    """
    A function that deletes a given event-user connection by id
    """
    dbc.del_one(GET_CONNECTS, filters={CUSER: uid, CEVENT: eid})
    return OK


def del_events_by_user(del_uid):
    """
    A function that deletes all events under a user's ownership
    """
    # dbc.del_many(GET_CONNECTS, filters={CUSER: del_uid})
    curr_connections = get_all_connections()
    for key, value in curr_connections:
        if value[CUSER] == del_uid:
            dbc.del_one(edata.GET_EVENTS, filters={edata.EVENTS: value[CEVENT]})
            dbc.del_one(GET_CONNECTS, filters={CONNECTIONS: key})
    return OK
