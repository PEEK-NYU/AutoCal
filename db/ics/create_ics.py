"""
This file will manipulate calendars, connect extsiting users to events and etc

"""
from ics import Calendar, Event
from datetime import datetime
from db import user_data
from db import connect_data
from db import event_data

cal = Calendar()

def create_event(organizer, title, start, end, desc, attendees = None, location = None):
    # TODO: Create event object with entered data....
    new_event = Event()

def add_to_cal(event, file):
    # TODO add given event to calendar file.
    # TODO LATER: Possibly check attendee list and connect existing AutoCal users to the event  ")
    
    with open('file', 'w') as my_file:
        my_file.writelines(cal)