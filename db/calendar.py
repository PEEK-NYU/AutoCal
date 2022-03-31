"""
file for exploring .ics capabilities and structures

Refrences:
https://pypi.org/project/icalendar/
https://fileinfo.com/extension/ics

TODO: maybe add to makefile? -->  pip install icalendar
(aslo for datetime)
"""

import icalendar
import datetime

import db.event_data as edata
from user_data import USERS, OK, NOT_FOUND, DUPLICATE


def get_ics(file):
    ...


def ics_parse(event):
    """
    Function to take in ICS Data and output
    """
    ...


def show_ics(info):
    ...
    

def cal_display(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()


def main():  # testing
    # TODO: finish testing
    print(".ics testing...")
    # terminal view ideas ---> $ icalendar view myfile.ics

    test_cal = icalendar.Calendar()
    test_cal['summary'] = "preliminary testing for icalendar functionality..."
    test_cal['dtstart'] = '20220313T000000'
    for k, v in tet_cal.items():  # test output
        print("Test_Cal Info:", k, v)
    print("Test_Cal tostring:\n", test_cal.to_ical())
    print("Fancy Cal Display:", cal_dispay(test_cal))
    
    test_event = icalendar.Event()
    startExpected = datetime(2021, 4, 4, 0, 0, 0, tzinfo=UTC)
    endExpected = datetime(2021, 4, 5, 0, 0, 0, tzinfo=UTC)
    test_event['summary'] = 'Test calendar'
    test_event['uid'] = '42'  # Naming?
    test_event.set('dtstart', date(2015, 4, 4))
    test_event.set('dtend', date(2015, 4, 5))
    
    test_cal.add_event(test_event)
    print("Cal Display:", cal_display(test_cal))
