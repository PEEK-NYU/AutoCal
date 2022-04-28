import pytest
from ics import Event
import db.ics.create_ics as c_ics


def test_create_event():
    new_cal = c_ics.create_event('Test organizer', 'Test title', '2022-02-02 00:00:00', '2022-02-02 00:00:00', 'Testing create_ics')
    assert isinstance(new_cal, Event)


def test_bad_create_event():
    with pytest.raises(Exception):
        new_cal = c_ics.create_event('Test organizer', 'Test title', '2022-02-02 00:00:00', 'Bad Date', 'Testing create_ics')
