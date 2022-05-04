"""
This file creates a a new event using users details
(Later) Parses users uploaded calendar to find open stimes
(Later) Displays suggests times to user
Manipulate calendars, connects extsiting users to events and
    stores event data in database
"""

# from ics import Calendar, Event
# from datetime import datetime
from db import user_data as udata
# from db import connect_data
from db import event_data as edata

# cal = Calendar()  # demo empty calendar

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


# def create_event(organizer, title, start, end, desc, attendees=None,
#                  location=None):  # noqa E501
#     """ ... """
#     # TODO: Create event object with entered data....
#     new_event = Event(name=title)
#     new_event.organizer = organizer
#     new_event.begin = start
#     new_event.end = end
#     new_event.description = desc
#     new_event.location = location
#     if attendees is not None:
#         if ',' in attendees:
#             att_lst = list(attendees.split(", "))
#             for persons in att_lst:
#                 new_event.add_attendee(persons)
#         else:
#             new_event.add_attendee(attendees)
#     return new_event
#
#
# def add_to_cal(event, file):
#     """ ... """
#     cal.events.add(event)
#     with open(file, 'w') as my_file:
#         my_file.writelines(cal)
#     return cal


def convert_event_dict(ics_data):
    """
    takes in ics data and returns a dict of event data
    returns {} on invalid ics_data
    Format:
    fake_e_data = {edata.ENAME: event_name, edata.STIME: start_time,
               edata.ETIME: end_time, edata.LOC: location,
               edata.DESC: description}
    """
    # event_data = {edata.ENAME: "", edata.STIME: "", edata.ETIME: "",
    #               edata.LOC: "", edata.DESC: ""}
    # TODO: finish
    return {}


def add_calendar(uid, ics_data):
    """ takes in a uid and ics data and imports an event """
    if not udata.user_exists(uid):
        return NOT_FOUND
    event_data = convert_event_dict(ics_data)
    if len(event_data) == 0:
        return NOT_FOUND
    edata.create_event(uid, event_data[edata.ENAME], event_data[edata.STIME],
                       event_data[edata.ETIME], event_data[edata.LOC],
                       event_data[edata.DESC])
    return OK
