"""
This file creates a a new event using users details

(Later) Parses users uploaded calendar to find open stimes

(Later) Displays suggests times to user

Manipulate calendars, connects extsiting users to events and stores event data in database


"""
from ics import Calendar, Event
from datetime import datetime
from db import user_data
from db import connect_data
from db import event_data

cal = Calendar() # demo empty calendar

def create_event(organizer, title, start, end, desc, attendees = None, location = None):
    # TODO: Create event object with entered data....
    new_event = Event(name=title)
    new_event.organizer = organizer
    new_event.begin = start 
    new_event.end = end
    new_event.description = desc
    new_event.location = location
    if attendees is not None:
        if ',' in attendees:
            att_lst = list(attendees.split(", "))
            for persons in att_lst:
                new_event.add_attendee(persons)
        
        else:
            new_event.add_attendee(attendees)

    return new_event
    

def add_to_cal(event, file):
    
    cal.events.add(event)
    with open(file, 'w') as my_file:
        my_file.writelines(cal)
    return cal