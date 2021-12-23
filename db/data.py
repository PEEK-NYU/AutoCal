"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

from bson.objectid import ObjectId, InvalidId

import db.db_connect as dbc

EVENTS = "events"
USERS = "users"
BREAKS = "breaks"

# field names in our DB:
USER_NM = "userName"
EVENTS_NM = "eventName"
ID = "_id"
BREAKS_NM = "breakName"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)


def get_breaks():
    """
    A function to return a dictionary of all breaks.
    """
    return dbc.fetch_all(BREAKS, ID)


def get_events():
    """
    A function to return a dictionary of all events.
    """
    return dbc.fetch_all(EVENTS, ID)


def event_exists(event_id):
    """
    Return True if event exists.
    """
    try:
        rec = dbc.fetch_one(EVENTS, filters={ID: ObjectId(event_id)})
        print(f"{rec=}")
        return rec is not None
    except (InvalidId, TypeError):
        return False


def break_exists(break_id):
    """
    Return True if event exists.
    """
    try:
        rec = dbc.fetch_one(BREAKS, filters={ID: ObjectId(break_id)})
        print(f"{rec=}")
        return rec is not None
    except (InvalidId, TypeError):
        return False


def del_event(event_id):
    """
    Delete a event from the database.
    """
    if not event_exists(event_id):
        return NOT_FOUND
    else:
        dbc.del_one(EVENTS, filters={ID: ObjectId(event_id)})
        return OK


def del_break(break_id):
    """
    Delete a break from the database.
    """
    if not break_exists(break_id):
        return NOT_FOUND
    else:
        dbc.del_one(BREAKS, filters={ID: ObjectId(break_id)})
        return OK


def add_event(eventname, location, start_time,
              end_time, description, owner, attendees):
    """
    Add a events to the events database.
    """
    print(f"{eventname=}")
    id = str(dbc.insert_doc(EVENTS,
                            {
                                "eventName": eventname,
                                "location": location,
                                "start_time": start_time,
                                "end_time": end_time,
                                "description": description,
                                "owner": owner,
                                "attendees": attendees
                            }).inserted_id)
    return {
        "status": OK,
        "id": id
    }


def add_break(breakname, start_time, end_time, owner):
    """
    Add a events to the events database.
    """
    print(f"{breakname=}")
    id = str(dbc.insert_doc(BREAKS,
                            {
                                "breakname": breakname,
                                "start_time": start_time,
                                "end_time": end_time,
                                "owner": owner,
                            }).inserted_id)
    return {
        "status": OK,
        "id": id
    }


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
        dbc.insert_doc(USERS, {
            USER_NM: username,
            "password": "dfdgdfgdsf",
            "google_key": "fdssdf2142323412",
            "profile_pic_url": "test.com/image"
        })
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
