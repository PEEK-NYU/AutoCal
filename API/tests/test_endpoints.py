from unittest import TestCase, skip
from flask_restx import Resource, Api
import random

import API.endpoints as ep
import db.db as db

HUGE_NUM = 10000000000000  # any big number will do!


def new_entity_name(entity_type):
    int_name = random.randint(0, HUGE_NUM)
    return f"new {entity_type}" + str(int_name)


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app(self):
        testrun = ep.AppTest(Resource)
        ret = testrun.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.WORKING_MSG, ret)

    @skip("In the middle of making this work.")
    def test_create_user(self):
        """
        See if we can successfully create a new user.
        Post-condition: user is in DB.
        """
        cu = ep.CreateUser(Resource)
        new_user = new_entity_name("user")
        ret = cu.create(new_user)
        users = db.get_users()
        self.assertIn(new_user, users)

    def test_create_event(self):
        """
        See if we can successfully create a new event.
        Post-condition: event is in DB.
        """
        cr = ep.CreateEvent(Resource)
        new_event = new_entity_name("room")
        ret = cr.create(new_event)
        events = db.get_events()
        self.assertIn(new_event, events)

    def event_test1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        lr = ep.ListEvents(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, dict)

    def event_test2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        lr = ep.ListEvents(Resource)
        ret = lr.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def event_test3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        lr = ep.ListEvents(Resource)
        ret = lr.get()
        for val in ret.values():
            self.assertIsInstance(val, dict)
