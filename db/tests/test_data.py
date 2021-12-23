"""
This file holds the tests for db.py.
"""

from unittest import TestCase
import random

import db.data as db

FAKE_USER = "Fake user"


HUGE_NUM = 10000000000000  # any big number will do!


def new_entity_name(entity_type):
    int_name = random.randint(0, HUGE_NUM)
    return f"new {entity_type}" + str(int_name)


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

    def test_add_event(self):
        """
        See if we can successfully create a new event.
        Post-condition: event is in DB.
        """
        new_event = new_entity_name("event")
        ret = db.add_event(new_event,
                           "testLoc",
                           1640146943,
                           1640146943,
                           "test descr",
                           "Paul",
                           ["Paul"])
        events = db.get_events()
        self.assertIn(ret['id'], events)

    def test_add_break(self):
        """
        See if we can successfully create a new breal.
        Post-condition: breal is in DB.
        """
        new_break = new_entity_name("break")
        breakItem = db.add_break(new_break, 1640146943, 1640146943, "Paul")
        breaks = db.get_breaks()
        self.assertIn(breakItem['id'], breaks)

    def test_get_users(self):
        """
        Can we fetch user db?
        """
        users = db.get_users()
        self.assertIsInstance(users, dict)

    def test_add_user(self):
        """
        Can we add a user to the db?
        """
        new_user = new_entity_name("user")
        db.add_user(new_user)
        users = db.get_users()
        self.assertIn(new_user, users)

    def test_del_user(self):
        """
        Can we delete a user from the db?
        """
        new_user = new_entity_name("user")
        db.add_user(new_user)
        db.del_user(new_user)
        users = db.get_users()
        self.assertNotIn(new_user, users)
