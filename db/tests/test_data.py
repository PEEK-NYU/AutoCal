"""
This file holds the tests for db
"""

from unittest import TestCase

import db.user_data as udata
import db.event_data as edata
import db.connect_data as cdata
import db.ics.create_ics as idata
import db.db_connect as dbc

import random
from bson.objectid import ObjectId

HUGE_NUM = 10000000000000  # (any big number)


def rand_name():
    """ randomized string method to doublecheck tests"""
    int_name = random.randint(0, HUGE_NUM)
    return " " + str(int_name)


# NOTICE: if a user-made event contains fake_key,
#         it will be deleted during testing
fake_key = "FAKE_KEY"

# fake user data
FAKE_USERNAME = "user name" + rand_name() + fake_key
UPDATED_FAKE_USERNAME = "user name" + rand_name() + fake_key
FAKE_PW = "password" + rand_name()
FAKE_EM = "test@testemail.com"
fake_u_data = {udata.UNAME: FAKE_USERNAME,
               udata.PW: FAKE_PW, udata.EM: FAKE_EM}

# fake event data
FAKE_ENAME = "event name" + rand_name() + fake_key
FAKE_START = "2022-3-29 12:00:00"  # TODO: find proper structure for this
FAKE_END = "2022-3-30 12:00:00"
FAKE_LOC = "Your Mom's House"
FAKE_DESC = "Watching Netflix"
fake_e_data = {edata.ENAME: FAKE_ENAME, edata.STIME: FAKE_START,
               edata.ETIME: FAKE_END, edata.LOC: FAKE_LOC,
               edata.DESC: FAKE_DESC}

FAKE_ics = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nBEGIN:VEVENT"\
           + "\nSUMMARY:Access-A-Ride Pickup\nDTSTART;TZID=America/New_York:20130802T103400" \
           + "\nDTEND;TZID=America/New_York:20130802T110400\nLOCATION:1000 Broadway Ave.\, Brooklyn" \
           + "\nDESCRIPTION: Access-A-Ride trip to 900 Jay St.\, Brooklyn" \
           + "\nSTATUS:CONFIRMED\nSEQUENCE:3\nBEGIN:VALARM\nTRIGGER:-PT10M\nDESCRIPTION:Pickup Reminder" \
           + "\nACTION:DISPLAY\nEND:VALARM\nEND:VEVENT\nEND:VCALENDAR"

# aggregation of data for endpoint testing
fake_data = [fake_u_data, fake_e_data, FAKE_ics]

client = dbc.get_client()  # global inst of client


class DBTestCase(TestCase):
    # Note: calls functions with 'test_' automatically!
    def setUp(self):
        # NOTE: clear_db and therefore udata.get_all_users() MUST WORK
        self.clear_db()  # clear past testing data

        # add test user
        self.test_uid = udata.add_user(FAKE_USERNAME, FAKE_PW, FAKE_EM)
        # print("Test User Created:", self.test_uid, "::", fake_data[0])

        # add test event
        self.test_eid = edata.create_event(self.test_uid, FAKE_ENAME,
                                           FAKE_START, FAKE_END,
                                           FAKE_LOC, FAKE_DESC)
        # print("Test Event Created:", self.test_eid, "::", fake_data[1])
        # print()

    def tearDown(self):
        self.clear_db()  # clear past testing data

    def admin_clear_db(self):
        """ clear all of db (not just test data) """
        client[dbc.db_nm][udata.GET_USERS].delete_many({})
        client[dbc.db_nm][edata.GET_EVENTS].delete_many({})
        client[dbc.db_nm][cdata.GET_CONNECTS].delete_many({})

    def clear_db(self):
        """ clear database of all past testing data for accuracy """
        for uid, user_info in udata.get_all_users().items():
            if fake_key in user_info[udata.UNAME]:
                # print("found user to delete!", user_info)
                # delete connection and users with fake_key in them
                client[dbc.db_nm][cdata.GET_CONNECTS].\
                    delete_many({cdata.CUSER: ObjectId(uid)})
                client[dbc.db_nm][udata.GET_USERS].\
                    delete_one({udata.USERS: ObjectId(uid)})
        for eid, event_info in edata.get_all_events().items():
            if fake_key in event_info[edata.ENAME]:
                # print("found event to delete!", event_info)
                client[dbc.db_nm][edata.GET_EVENTS].\
                    delete_one({edata.EVENTS: ObjectId(eid)})

        # print("**User, Event, & Connects DB Cleared**")

    # USER TESTS
    def test_get_users(self):
        """ Can we fetch user db? """
        users = udata.get_all_users()
        self.assertIsInstance(users, dict)
        # print("Found All Users:", users)
        # from command line, type: python -c 'import user_data;
        # print(user_data.get_all_users())'

    def test_create_user(self):
        """ Was the user creation okay? """
        self.assertIsNot(self.test_uid, udata.NOT_FOUND)
        # print("User Created:", self.test_uid)

    def test_user_exists(self):
        """ does the created user exist? """
        result = udata.user_exists(self.test_uid)
        self.assertIsNot(result, udata.NOT_FOUND)
        # print("User Found:", result)

    def test_user_data(self):
        """ can we access the correct info of a user? """
        test_data = udata.get_user(self.test_uid)
        for key, value in fake_u_data.items():
            self.assertEquals(test_data[key], value)
        # print("User Data Found:", test_data)

    def test_find_user(self):
        """ can we find our user via keyword? """
        our_user = udata.find_user(fake_key)
        self.assertIn(self.test_uid, our_user.keys())

    def test_login(self):
        """ can we log into a user? """
        logged = udata.log_in(FAKE_USERNAME, FAKE_PW)
        self.assertEquals(self.test_uid, logged)
        # print("User", FAKE_USERNAME, "logged in!")

    def test_get_emails(self):
        """ can we find our email in the set of all emails? """
        ems = udata.get_emails()
        self.assertIn(FAKE_EM, ems)

    def test_email_exists(self):
        """ can we make sure our specific email exists? """
        self.assertEquals(udata.OK, udata.email_exists(FAKE_EM))

    def test_valid_email(self):
        """ is our email validation working? """
        self.assertEquals(udata.OK, udata.valid_email(FAKE_EM))
        self.assertEquals(udata.OK, udata.valid_email(FAKE_EM+rand_name()))
        self.assertEquals(udata.NOT_FOUND, udata.valid_email("bademail"))

    # def test_update_username(self):
    #     """ can we update our user's username and login with the new version? """
    #     ret = udata.update_username(self.test_uid, UPDATED_FAKE_USERNAME)
    #     self.assertEquals(ret, udata.OK)
    #     logged = udata.log_in(UPDATED_FAKE_USERNAME, FAKE_PW)
    #     self.assertEquals(self.test_uid, logged)

    # EVENT TESTS
    def test_get_events(self):
        """ Can we fetch event db? """
        events = edata.get_all_events()
        self.assertIsInstance(events, dict)
        # print("Found All Events:", events)

    def test_create_event(self):
        """ Was the event creation okay? """
        self.assertIsNot(self.test_eid, edata.NOT_FOUND)
        # print("Event Created:", self.test_eid)

    def test_event_exists(self):
        """ does the created event exist? """
        result = edata.event_exists(self.test_eid)
        self.assertIsNot(result, edata.NOT_FOUND)
        # print("Event Found:", result)

    def test_event_data(self):
        """ can we access the correct info of a user? """
        test_data = edata.get_event(self.test_eid)
        for key, value in fake_e_data.items():
            self.assertEquals(test_data[key], value)
        # print("Event Data Found:", test_data)

    def test_get_event_by_user(self):
        """ can we get an event from our user id """
        temp_events = edata.get_user_events(self.test_uid)
        self.assertIn(self.test_eid, temp_events.keys())

    def test_get_event_by_keyword(self):
        """ can we get an event from our user id """
        temp_events = edata.find_event(self.test_uid, fake_key)
        self.assertIn(self.test_eid, temp_events.keys())

    # CONNECT TESTS
    def test_connection(self):
        """
        test that the connection made between our test event and user exists
        """
        self.assertTrue(cdata.is_connected(self.test_eid, self.test_uid))

    def test_get_connection(self):
        """ test that we can find our connection in all connections """
        connects = cdata.get_all_connections()
        fake_cdata = {cdata.CUSER: self.test_uid, cdata.CEVENT: self.test_eid}
        self.assertIn(fake_cdata, connects.values())

    def test_connection_eid(self):
        """ test that we can access our connection via eid """
        self.assertEquals(self.test_uid, cdata.get_connection_from_eid(self.test_eid))

    def test_ics(self):
        """ testing that ics parsing works """
        test_cal = idata.add_calendar(self.test_uid, FAKE_ics)
        self.assertNotEqual(test_cal, udata.NOT_FOUND)

    # DELETION TESTS
    def test_del_event(self):
        """
        see if we can delete our test event
        and its corresponding connection
        """
        deleted = edata.del_event(self.test_eid, self.test_uid)
        self.assertNotIn(self.test_eid, edata.get_all_events().keys())
        self.assertFalse(cdata.is_connected(self.test_eid, self.test_uid))

    def test_del_user(self):
        """ see if we can delete our test user """
        deleted = udata.del_user(self.test_uid)
        self.assertNotIn(self.test_uid, udata.get_all_users().keys())
