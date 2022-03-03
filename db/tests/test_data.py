"""
This file holds the tests for db
"""

from unittest import TestCase, skip
# import random
# import db.data as db

import db.user_data as udata
import db.event_data as edata
import db.connect_data as cdata

FAKE_USER = "fake uid"
FAKE_USERNAME = "fake name"
FAKE_PW = "fake password"


class DBTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_write_collection(self):
        """
        Can we write the user db?
        """
        fake_data = {FAKE_USER: {udata.UNAME: FAKE_USERNAME,
                                 udata.PW: FAKE_PW}}
        return True

    def test_get_users(self):
        """
        Can we fetch user db?
        """
        users = udata.get_all_users()
        self.assertIsInstance(users, dict)

    def test_get_events(self):
        """
        Can we fetch event db?
        """
        rooms = edata.get_all_events()
        self.assertIsInstance(rooms, dict)
