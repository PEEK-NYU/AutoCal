# import pytest
# import json
from ics import Event
import db.ics.create_ics as c_ics

from unittest import TestCase  # , skip


class DBICSTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_create_event(self):
        """
        Testing create_event() with good inputs
        """
        new_cal = c_ics.create_event('Test organizer', 'Test title', '2022-02-02 00:00:00', '2022-02-02 00:00:00', 'Testing create_ics')
        self.assertTrue(isinstance(new_cal, Event))


    def test_bad_create_event(self):
        """
        Testing create_event() with a bad date input as date must follow a specific format
        """
        new_cal = c_ics.create_event('Test organizer', 'Test title', '2022-02-02 00:00:00', 'Bad Date', 'Testing create_ics')

    def test_convert_event_dict(self):
        """
        Convert ics to dict
        """
        new_event_dict = c_ics.convert_event_dict('demo_calendar.ics')
        self.assertTrue(isinstance(new_event_dict, dict))

    def test_uid_add_calendar(self):
        """
        TODO: add_calendar must be properly defined or create skeleton
        """
        good_uid = '6223ba54024eb2d8c26fc0cd'
        good_ics_data = 'demo_calendar.ics'

    def test_bad_uid_add_calendar(self):
        """
        Testing create_event() with good inputs
        """
        bad_uid = '12345678'
        good_ics_data = 'demo_calendar.ics'
