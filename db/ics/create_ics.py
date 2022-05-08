"""
This file creates a a new event using users details
(Later) Parses users uploaded calendar to find open stimes
(Later) Displays suggests times to user
Manipulate calendars, connects extsiting users to events and
    stores event data in database
"""

# from ics import Calendar, Event
# from datetime import datetime
# from db import connect_data
from db import event_data as edata
import jicson
# Python ICS to JSon library @ https://github.com/CalyFactory/python-jicson

# cal = Calendar()  # demo empty calendar

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


def convert_event_dict(ics_data):
    """
    takes in ics data and returns a dict of event data
    returns {} on invalid ics_data
    Format:
    fake_e_data = {edata.ENAME: event_name, edata.STIME: start_time,
               edata.ETIME: end_time, edata.LOC: location,
               edata.DESC: description}
    """
    if ics_data[-3:] == "ics" or ics_data[-3:] == "DAR":
        if ics_data[-3:] == "ics":
            result = jicson.fromFile(ics_data)
        else:
            result = jicson.fromText(ics_data)
        cal = result['VCALENDAR']
        events = cal[0]['VEVENT']
        if len(events) > 0:
            for event in events:
                dtstart = 'DTSTART'
                dtend = 'DTEND'
                for key in event.keys():
                    if key.find('DTSTART') > -1:
                        dtstart = key
                    elif key.find('DTEND') > -1:
                        dtend = key
                event_data = {edata.ENAME: event['SUMMARY'],
                              edata.STIME: event[dtstart],
                              edata.ETIME: event[dtend],
                              edata.LOC: event['LOCATION'],
                              edata.DESC: event['DESCRIPTION']}
                yield event_data
        else:
            yield {}
    else:
        yield{}


def add_calendar(uid, ics_data):
    """
    takes in a uid and ics data and imports an event
    returns input data on success
    """
    has_imported = False
    input_data = []
    for event_data in convert_event_dict(ics_data):
        if len(event_data) == 0:  # bool checks if empty
            if has_imported:
                return input_data
            else:
                return NOT_FOUND
        input_data.append(event_data)
        edata.create_event(uid, event_data[edata.ENAME],
                           event_data[edata.STIME],
                           event_data[edata.ETIME], event_data[edata.LOC],
                           event_data[edata.DESC])
        has_imported = True
    return input_data
