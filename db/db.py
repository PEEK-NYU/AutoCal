"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

PEEK_DIR = os.environ["PEEK_DIR"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    DB_DIR = f"{PEEK_DIR}/db/test_dbs"
else:
    DB_DIR = f"{PEEK_DIR}/db"

EVENTS_DB = f"{PEEK_DIR}/db/events.json"
USERS_DB = f"{PEEK_DIR}/db/users.json"


shell_event = {"name": "Software Engineering: CS-UY 4513-C",
               "descr": "",
               "start_time": 0,  # thoughts of datetime.Ticks conversion
               "end_time": 0,
               "duration": 0,
               "location": "2 Metrotech",
               "unscheduled": False,
               "attendees": []}
OK = 0
NOT_FOUND = 1
DUPLICATE = 2


def write_collection(perm_version, mem_version):
    """
    Write out the in-memory data collection in proper DB format.
    """
    with open(perm_version, 'w') as f:
        json.dump(mem_version, f, indent=4)


def read_collection(perm_version):
    """
    A function to read a colleciton off of disk.
    """
    try:
        with open(perm_version) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print(f"{perm_version} not found.")
        return None


def get_events():
    """
    A function to return a dictionary of all events.
    """
    return read_collection(EVENT_COLLECTION)


def get_users():
    """
    A function to return a dictionary of all users.
    """
    return read_collection(USER_COLLECTION)


def add_event(eventname):
    """
    Add a events to the events database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    events = get_events()
    like_events = find_name(events, eventname)
    if len(like_events) != 0:
        print(len(like_events), "other events with this name:\n",
              like_events)
        # maybe add some more interaction where the user is shown
        # the list of the like events and is given the option
        # to edit one that they have edit-access instead
    if events is None:
        return NOT_FOUND
    else:
        events[eventname] = {"num_users": 0}
        write_collection(EVENT_COLLECTION, events)
        return OK
        
    
def find_name(collection, name):
    """
    A function that returns a list of ids...
    within a collection by "name".
    """
    found_lst = []
    for key, value in collection.items():
        if value["name"] == name:
            found_lst.append(key)
    return found_lst


def add_user(username):
    """
    Add a user to the user database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    users = get_users()
    if users is None:
        return NOT_FOUND
    elif username in users:
        return DUPLICATE
    else:
        users[username] = {}
        write_collection(USER_COLLECTION, users)
        return OK
