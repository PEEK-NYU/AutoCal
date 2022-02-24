"""
This file holds the tests for endpoints.py.
"""

from unittest import TestCase, skip 
from flask_restx import Resource, Api
import random

import API.endpoints as ep
import db.data as db

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
        self.assertIn(ep.HELLO, ret)

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
        self.assertIn(new_user, users)

    @skip("In the middle of making this work.")
    def test_create_event(self):
        """
        See if we can successfully create a new event.
        Post-condition: room is in DB.
        """
        cr = ep.CreateRoom(Resource)
        new_room = new_entity_name("room")
        ret = cr.post(new_room)
        print(f'post {ret=}')
        rooms = db.get_rooms_as_dict()
        print(f'{rooms=}')
        self.assertIn(new_room, rooms)
