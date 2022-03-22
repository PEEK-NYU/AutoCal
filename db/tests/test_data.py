"""
This file holds the tests for db
"""

from unittest import TestCase, skip
# import random
# import db.data as db

import db.user_data as udata
import db.event_data as edata
import db.connect_data as cdata

FAKE_USERNAME = "fake name"
FAKE_PW = "fake password"
fake_data = {udata.UNAME: FAKE_USERNAME, udata.PW: FAKE_PW}


class DBTestCase(TestCase):
    def setUp(self):
        """ test creates, exists, and updates """
        new_uid = ""
        new_eid = ""

        # test user
        self.test_get_users()

        new_uid = self.test_create_user()
        assert new_uid != udata.NOT_FOUND

        assert self.test_exists_user(new_uid) == udata.OK
        assert self.test_user_data(new_uid, fake_data) == udata.OK
        assert self.test_login(new_uid, FAKE_USERNAME, FAKE_PW)

        # test event
        self.test_get_events()

    def tearDown(self):
        """ test deletes -w- exists """
        pass

    def test_get_users(self):
        """
        Can we fetch user db?
        """
        users = udata.get_all_users()
        self.assertIsInstance(users, dict)

    def test_create_user(self):
        """
        Can we write the user db?
        """
        user_create_result = udata.add_user(FAKE_USERNAME, FAKE_PW)
        if user_create_result == udata.NOT_FOUND:
            return user_create_result
        return user_create_result

    def test_user_exists(self, test_uid):
        """
        does a user exist?
        """
        user_exists_result = udata.user_exists(test_uid)
        if user_exists_result == udata.NOT_FOUND:
            return user_exists_result
        return udata.OK

    def test_user_data(self, test_uid, data):
        """
        can we access the correct info of a user?
        """
        test_data = udata.get_user(test_uid)
        for key, value in data.items():
            if test_data[key] != value:
                return udata.NOT_FOUND
        return udata.OK

    def test_login(self, uid, user_name, pass_word):
        """
        can we log into a user?
        """
        logged = udata.log_in(user_name, pass_word)
        if logged != uid:
            return udata.NOT_FOUND
        return udata.OK

    def test_get_events(self):
        """
        Can we fetch event db?
        """
        events = edata.get_all_events()
        self.assertIsInstance(events, dict)

    def test_create_event(self):
        """
        Can we write to the user db?
        """
        pass
