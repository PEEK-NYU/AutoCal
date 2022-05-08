"""
This file creates a a new event using users details
(Later) Parses users uploaded calendar to find open stimes
(Later) Displays suggests times to user
Manipulate calendars, connects extsiting users to events and
    stores event data in database
"""

#from ics import Calendar, Event
#from datetime import datetime
from db import user_data as udata
# from db import connect_data
from db import event_data as edata
import jicson # Python ICS to JSon library @ https://github.com/CalyFactory/python-jicson

#cal = Calendar()  # demo empty calendar

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


#def create_event(organizer, title, start, end, desc, attendees=None,
#                 location=None):  # noqa E501
#    """ 
#    Create event object with user's event details 
#    """
#    new_event = Event(name=title)
#    new_event.organizer = organizer
#    new_event.begin = start
#    new_event.end = end
#    new_event.description = desc
#    new_event.location = location
#    if attendees is not None:
#        if ',' in attendees:
#            att_lst = list(attendees.split(", "))
#            for persons in att_lst:
#                new_event.add_attendee(persons)
#        else:
#            new_event.add_attendee(attendees)
#    return new_event
#
#
#def add_to_cal(event, user_ics_data):
#    """ 
#    Add event to user ics file 
#    """
#    cal.events.add(event)
#    with open(user_ics_data, 'w') as my_file:
#        my_file.writelines(cal)
#    return cal

def convert_event_dict(ics_data):
    """
    takes in ics data and returns a dict of event data
    returns {} on invalid ics_data
    Format:
    fake_e_data = {edata.ENAME: event_name, edata.STIME: start_time,
               edata.ETIME: end_time, edata.LOC: location,
               edata.DESC: description}
    """
    result = jicson.fromFile(ics_data)
    cal = result['VCALENDAR']
    events = cal[0]['VEVENT']
    event_date = {}  # @beth what is this used for?
    if len(events)>0:
        for event in events:
            event_data = {edata.ENAME: event['SUMMARY'], edata.STIME: event['DTSTART'], edata.ETIME: event['DTEND'],
                        edata.LOC: event['LOCATION'], edata.DESC: event['DESCRIPTION']}
            yield event_data
    else:
        yield {}

def add_calendar(uid, ics_data):
    """ takes in a uid and ics data and imports an event """
    if not udata.user_exists(uid):
        return NOT_FOUND

    # if len(event_data) == 0:
    #     return NOT_FOUND
    has_imported = False
    for event_data in convert_event_dict(ics_data):
        if bool(event_data):  # bool checks if empty
            if has_imported:
                return OK
            else:
                return NOT_FOUND
        edata.create_event(uid, event_data[edata.ENAME], event_data[edata.STIME],
                           event_data[edata.ETIME], event_data[edata.LOC],
                           event_data[edata.DESC])
        has_imported = True
    return OK
