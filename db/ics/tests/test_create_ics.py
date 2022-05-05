import pytest
import json
from ics import Event
import db.ics.create_ics as c_ics


def test_create_event():
    """
    Testing create_event() with good inputs
    """
    new_cal = c_ics.create_event('Test organizer', 'Test title', '2022-02-02 00:00:00', '2022-02-02 00:00:00', 'Testing create_ics')
    assert isinstance(new_cal, Event)


def test_bad_create_event():
    """
    Testing create_event() with a bad date input as date must follow a specific format
    """
    with pytest.raises(Exception):
        new_cal = c_ics.create_event('Test organizer', 'Test title', '2022-02-02 00:00:00', 'Bad Date', 'Testing create_ics')

def test_convert_event_dict():
    """
    Convert ics to dict
    """
    new_event_dict = c_ics.convert_event_dict('./demo_calendar.ics')
    assert isinstance(new_event_dict,dict)

def test_uid_add_calendar(): 
    """ 
    TODO: add_calendar must be properly defined or create skeleton
    """
    good_uid = '6223ba54024eb2d8c26fc0cd'
    good_ics_data = 'demo_calendar.ics'

def test_bad_uid_add_calendar():
    """
    Testing create_event() with good inputs
    """
    bad_uid = '12345678'
    good_ics_data = 'demo_calendar.ics'