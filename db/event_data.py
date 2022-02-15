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

DEMO_HOME = os.environ["DEMO_HOME"]
GET_EVENTS = "events"
EVENTS = "_event_id"
ENAME = "eventname"
STIME = "start_time"
ETIME =  "end_time"
LOC = "location"
DESC = "description"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

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
        return generate_uid()  # recursively make sure no repeat uid's
    return new_uid

