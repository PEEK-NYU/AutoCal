"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

DB_DIR = os.environ["PEEK_DIR"]

EVENTS_DB = f"{PEEK_DIR}/db/events.json"
USERS_DB = f"{PEEK_DIR}/db/users.json"

shell_event = {"name": "Software Engineering: CS-UY 4513-C", "descr": "",
"start_time":0, "end_time": 0, "duration": 90, "location": "2 Metrotech",
 "unscheduled": False, "attendees": []}

def write_events(events):
    with open(EVENTS_DB, 'w') as f:
        json.dump(events, f, indent=4)


def write_users(users):
    with open(USERS_DB, 'w') as f:
        json.dump(users, f, indent=4)
    
    
def get_events_by_name(event_name):
    events = get_events()
    temp_events = []
    for key, value in events:
        if value["name"] == event_name:
            temp_events.append(key)
    return temp_events


def get_events():
    """
    A function to return all chat rooms.
    """
    try:
        with open(EVENTS_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print("Rooms db not found.")
        return None


def num_events():
    """
    A function to return the number of events in the db.
    Secondary usage to help with ID generation
    """
    events = get_events()
    return len(events)


def add_event():
    """
    Add an infoless, unique event to the room database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    if events is None:
        return NOT_FOUND
    else:
        events[num_events()+1] = shell_event
        
        
def add_event_by_name(eventname):
    """
    Add an event to the room database by name.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    events = get_events()
    
    if events is None:
        return NOT_FOUND
    elif eventname in events:
        return DUPLICATE
    else:
        new_event = shell_event
        new_event["name"] = eventname
        events[num_events()+1] = new_event
        write_rooms(rooms)
        return OK
