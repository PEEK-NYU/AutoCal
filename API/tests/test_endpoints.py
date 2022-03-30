"""
This file holds the tests for endpoints.py
"""

from unittest import TestCase, skip
from flask_restx import Resource, Api
import random

import API.endpoints as ep

import db.user_data as udata
import db.event_data as edata
import db.connect_data as cdata

HUGE_NUM = 10000000000000  # any big number will do!


def new_entity_name(entity_type):
    int_name = random.randint(0, HUGE_NUM)
    return f"new {entity_type}" + str(int_name)


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.test_key, ret)

    def test_create_user(self):
        """
        See if we can successfully create a new user.
        Post-condition: user is in DB.
        """
        cu = ep.CreateUser(Resource)
        new_user = new_entity_name("user")
        new_pw = new_entity_name("password")
        ret = cu.post(new_user, new_pw)
        users = udata.get_all_users()
        self.assertIn(ret, users.keys())
        return ret  # for using uid in other testing context

    # @skip("In the middle of making this work.")
    def test_create_event(self):
        """
        See if we can successfully create a new event.
        Post-condition: room is in DB.
        """
        uid = self.test_create_user()
        cr = ep.CreateEvent(Resource)
        event_name = new_entity_name("event")
        start_time = new_entity_name("start")
        end_time = new_entity_name("end")
        ret = cr.post(uid, event_name, start_time, end_time)
        # print(f'post {ret=}')
        events = edata.get_all_events()
        # print(f'{events=}')
        self.assertIn(ret, events.keys())
