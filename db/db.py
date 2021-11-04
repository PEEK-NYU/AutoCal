"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

DEMO_HOME = os.environ["DEMO_HOME"]

EVENTS_DB = f"{DEMO_HOME}/db/events.json"
# Note: we save events to preserve the possibility of multiple users containing the same event

def get_rooms():
    """
    A function to return all events in database.
    """
    try:
        with open(EVENTS_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None
