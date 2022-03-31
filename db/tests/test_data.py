"""
This file holds the tests for db
"""

from unittest import TestCase

import db.user_data as udata
import db.event_data as edata
import db.connect_data as cdata

# fake user data
FAKE_USERNAME = "fake name"
FAKE_PW = "fake password"
FAKE_EM = "test@testemail.com"
fake_u_data = {udata.UNAME: FAKE_USERNAME,
               udata.PW: FAKE_PW, udata.EM: FAKE_EM}

# fake event data
FAKE_ENAME = "fake event"
FAKE_START = "2022-3-29 12:00:00"  # TODO: find proper structure for this
FAKE_END = "2022-3-30 12:00:00"
FAKE_LOC = "Your Mom's House"
FAKE_DESC = "Watching Netflix"
fake_e_data = {edata.ENAME: FAKE_ENAME, edata.STIME: FAKE_START,
               edata.ETIME: FAKE_END, edata.LOC: FAKE_LOC,
               edata.DESC: FAKE_DESC}


class DBTestCase(TestCase):
    # Note: calls functions with 'test_' automatically!
    def setUp(self):
        self.clear_db()  # clear database of all data

        # add test user
        self.test_uid = udata.add_user(FAKE_USERNAME, FAKE_PW, FAKE_EM)
        # add test event
        self.test_eid = edata.create_event(self.test_uid, FAKE_ENAME,
                                           FAKE_START, FAKE_END,
                                           FAKE_LOC, FAKE_DESC)

    def tearDown(self):
        self.clear_db()  # clear database of all data

    def clear_db(self):
        """ clear database of all data for testing """
        # TODO: complete
        pass

    # USER TESTS
    def test_get_users(self):
        """ Can we fetch user db? """
        users = udata.get_all_users()
        self.assertIsInstance(users, dict)
        print("Found All Users:", users)

    def test_create_user(self):
        """ Was the user creation okay? """
        self.assertIsNot(self.test_uid, udata.NOT_FOUND)
        print("User Created:", self.test_uid)

    def test_user_exists(self):
        """ does the created user exist? """
        result = udata.user_exists(self.test_uid)
        self.assertIsNot(result, udata.NOT_FOUND)
        print("User Found:", result)

    def test_user_data(self):
        """ can we access the correct info of a user? """
        test_data = udata.get_user(self.test_uid)
        for key, value in fake_u_data.items():
            self.assertIs(test_data[key], value)
        print("User Data Found:", test_data)

    def test_login(self):
        """ can we log into a user? """
        logged = udata.log_in(FAKE_USERNAME, FAKE_PW)
        self.assertIs(self.test_uid, logged)
        print("User", FAKE_USERNAME, "logged in!")

    # EVENT TESTS
    def test_get_events(self):
        """ Can we fetch event db? """
        events = edata.get_all_events()
        self.assertIsInstance(events, dict)
        print("Found All Events:", events)

    def test_create_event(self):
        """ Was the event creation okay? """
        self.assertIsNot(self.test_eid, edata.NOT_FOUND)
        print("Event Created:", self.test_eid)

    def test_event_exists(self):
        """ does the created event exist? """
        result = edata.event_exists(self.test_eid)
        self.assertIsNot(result, edata.NOT_FOUND)
        print("Event Found:", result)

    def test_event_data(self):
        """ can we access the correct info of a user? """
        test_data = edata.get_event(self.test_eid)
        for key, value in fake_e_data.items():
            self.assertIs(test_data[key], value)
        print("Event Data Found:", test_data)

    def test_connection(self):
        """
        test that the connection made between our test event and user exists
        """
        self.assert_(cdata.is_connected(self.test_eid, self.test_uid))
