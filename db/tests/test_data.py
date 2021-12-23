"""
This file holds the tests for db.py.
"""

from unittest import TestCase
# import random

import db.data as db

FAKE_USER = "Fake user"


class DBTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_write_collection(self):
        """
        Can we write the user db?
        """
        fake_data = {FAKE_USER: {}}
        return True

    def test_get_users(self):
        """
        Can we fetch user db?
        """
        users = db.get_users()
        self.assertIsInstance(users, dict)

    def test_get_breaks(self):
        """
        Can we fetch breaks db?
        """
        breaks = db.get_breaks()
        self.assertIsInstance(breaks, dict)

    def test_get_events(self):
        """
        Can we fetch events db?
        """
        events = db.get_events()
        self.assertIsInstance(events, dict)

    def test_event_exist(self):
        """
        Can we fetch if an event exists
        """
        event = db.add_event("testEvent",
                             "testLoc",
                             1640146943,
                             1640146943,
                             "test descr",
                             "Paul",
                             ["Paul"])
        event_exists = db.event_exists(event['id'])
        self.assertTrue(event_exists)

    def test_break_exist(self):
        """
        Can we fetch if a break exists
        """
        breakItem = db.add_break("testEvent", 1640146943, 1640146943, "Paul")
        break_exists = db.break_exists(breakItem['id'])
        self.assertTrue(break_exists)

    def test_del_event(self):
        """
        Can we delete an event
        """
        event = db.add_event("testEvent",
                             "testLoc",
                             1640146943,
                             1640146943,
                             "test descr",
                             "Paul",
                             ["Paul"])
        db.del_event(event['id'])
        events = db.get_events()
        self.assertFalse((event['id'] in events))

    def test_del_break(self):
        """
        Can we delete a break
        """
        breakItem = db.add_break("testEvent", 1640146943, 1640146943, "Paul")
        db.del_break(breakItem['id'])
        breaks = db.get_breaks()
        self.assertFalse((breakItem['id'] in breaks))
