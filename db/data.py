"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import os

import db.db_connect as dbc

EVENTS = "events"
USERS = "users"

# field names in our DB:
USER_NM = "userName"
EVENTS_NM = "eventName"
NUM_USERS = "num_users"

'''
Could be unecessary

EVENTS_LOCATION = "eventLocation"
EVENTS_DURATION = "eventDuration"
EVENTS_START_TIME = "eventStartTime"
EVENTS_END_TIME = "eventEndTime"
'''

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)

def get_events():
    """
    A function to return a dictionary of all events.
    """
    return dbc.fetch_all(EVENTS, EVENTS_NM)

def event_exists(event_name):
    """
    Return True if event exists.
    """
    rec = dbc.fetch_one(EVENTS, filters={EVENTS_NM: event_name})
    print(f"{rec=}")
    return rec is not None

def del_event(event_name):
    """
    Delete a event from the database.
    """
    if not event_exists(event_name):
        return NOT_FOUND
    else:
        dbc.del_one(EVENTS, filters={EVENTS_NM: event_name})
        return OK

def add_event(event_traits):
    """
    Add a events to the events database.
    - event_traits is a collection of info for the event
    - event_traits must include "name" for now
    """
    events = get_events()
    print(f"{event_traits['name']=}")
    if event_exists(event_traits['name']):
        return DUPLICATE
    else:
        dbc.insert_doc(EVENTS, {
            EVENTS_NM: event_traits['name']
        })
        return OK
    
'''
def set_event_fields(event_traits):
    """
    Set fields of an existing event.
    - event_traits is a collection of info for the event
    - event_traits must include "name" for now
    """
    events = get_events()
    print(f"{event_traits['name']=}")
    if not(event_exists(event_traits['name'])):
        return NOT_FOUND
    else:
        newvals = {"$set": {}}
        for key in event_traits:
            if key == "name":
                filters = {"name": event_traits[key]}
            else:
                newvals["$set"][key] = event_traits[key]  
        dbc.update_one(EVENTS, filters, newvals)
        return OK

def set_user_fields(user_traits):
    """
    Set fields of an existing user.
    - user_traits is a collection of info for the user
    - user_traits must include "name" for now
    """
    users = get_users()
    print(f"{user_traits['name']=}")
    if not(user_exists(user_traits['name'])):
        return NOT_FOUND
    else:
        newvals = {"$set": {}}
        for key in user_traits:
            if key == "name":
                filters = {"name": user_traits[key]}
            else:
                newvals["$set"][key] = user_traits[key]  
        dbc.update_one(USERS, filters, newvals)
        return OK
'''

def get_users():
    """
    A function to return a dictionary of all users.
    """
    return dbc.fetch_all(USERS, USER_NM)

def user_exists(username):
    """
    See if a user with username is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(USERS, filters={USER_NM: username})
    print(f"{rec=}")
    return rec is not None

def add_user(username):
    """
    Add a user to the user database.
    """
    if user_exists(username):
        return DUPLICATE
    else:
        dbc.insert_doc(USERS, {USER_NM: username})
        return OK

def del_user(username):
    """
    Delete username from the db.
    """
    if not user_exists(username):
        return NOT_FOUND
    else:
        dbc.del_one(USERS, filters={USER_NM: username})
        return OK

# function templates/shells for integration with google cal
def get_scheduling_options(user_schedule, common_events):
    """
    Input: the user's schedule for the requested time range
    Input: list of other scheduled events of the same type/group
    Output: list of recommended event times
    """
    return
