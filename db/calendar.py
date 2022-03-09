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
    ...


def show_ics(info):
    ...


def main():  # testing
    print(".ics testing...")

    test_event = icalendar.Event()
    startExpected = datetime(2021, 4, 4, 0, 0, 0, tzinfo=UTC)
    endExpected = datetime(2021, 4, 5, 0, 0, 0, tzinfo=UTC)
    test_event['summary'] = 'Test calendar'
    test_event['uid'] = '42'  # Naming?
    test_event.set('dtstart', date(2015, 4, 4))
    test_event.set('dtend', date(2015, 4, 5))