"""
This file holds the tests for endpoints.py
"""

from unittest import TestCase, skip
from flask_restx import Resource, Api


import API.endpoints as ep

import db.user_data as udata
import db.event_data as edata
import db.connect_data as cdata

from db.tests.test_data import fake_data


class EndpointTestCase(TestCase):
    def setUp(self):
        self.clear_db()  # clear database of all data

        # add test user
        cu = ep.CreateUser(Resource)
        self.test_uid = cu.post(fake_data[0][udata.UNAME],
                                fake_data[0][udata.PW],
                                fake_data[0][udata.EM])
        # add test event
        ce = ep.CreateEvent(Resource)
        self.test_eid = ce.post(self.test_uid,
                                fake_data[1][edata.ENAME],
                                [fake_data[1][edata.STIME],
                                 fake_data[1][edata.ETIME]],
                                fake_data[1][edata.LOC],
                                fake_data[1][edata.DESC])

    def tearDown(self):
        self.clear_db()  # clear database of all data

    def clear_db(self):
        """ clear database of all data for testing """
        # TODO: complete
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
        users = udata.get_all_users()
        self.assertIn(self.test_uid, users.keys())

    # @skip("In the middle of making this work.")
    def test_create_event(self):
        """
        See if we can successfully create a new event.
        Post-condition: room is in DB.
        """
        events = edata.get_all_events()
        self.assertIn(self.test_eid, events.keys())
