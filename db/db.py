"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

def get_event():
    """
    A function to return all events in the data store.
    """
    return {"event_ID": 1234,
    "name": "Software Engineering",
    "start_time": 1636038000,
    "end_time": 1636043400,
    "duration": 90,
    "location": "Bern Dibner",
    "unscheduled": False}