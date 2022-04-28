"""
This file holds the tests for endpoints.py
"""

from unittest import TestCase  # , skip
from flask_restx import Resource  # , Api


import API.endpoints as ep

import db.user_data as udata
import db.event_data as edata
import db.connect_data as cdata
import db.db_connect as dbc

from db.tests.test_data import fake_data, fake_key
from bson.objectid import ObjectId

client = dbc.get_client()  # global inst of client


class EndpointTestCase(TestCase):
    def setUp(self):
        self.clear_db()  # clear database of all data

        # add test user
        cu = ep.CreateUser(Resource)
        self.test_uid = cu.post(fake_data[0][udata.UNAME],
                                fake_data[0][udata.PW],
                                fake_data[0][udata.EM])
        # print("Test User Created:", self.test_uid, "::", fake_data[0])

        # add test event
        ce = ep.CreateEvent(Resource)
        self.test_eid = ce.post(self.test_uid,
                                fake_data[1][edata.ENAME],
                                fake_data[1][edata.STIME],
                                 fake_data[1][edata.ETIME],
                                # fake_data[1][edata.LOC],
                                fake_data[1][edata.DESC])
        # print("Test Event Created:", self.test_eid, "::", fake_data[1])
        # print()

    def tearDown(self):
        self.clear_db()  # clear database of all data

    def clear_db(self):
        """ clear database of all past testing data for accuracy """
        for uid, user_info in udata.get_all_users().items():
            if fake_key in user_info[udata.UNAME]:
                # print("found user to delete!", user_info)
                # delete connection and users with fake_key in them
                client[dbc.db_nm][cdata.GET_CONNECTS]. \
                    delete_many({cdata.CUSER: ObjectId(uid)})
                client[dbc.db_nm][udata.GET_USERS]. \
                    delete_one({udata.USERS: ObjectId(uid)})
        for eid, event_info in edata.get_all_events().items():
            if fake_key in event_info[edata.ENAME]:
                # print("found event to delete!", event_info)
                client[dbc.db_nm][edata.GET_EVENTS]. \
                    delete_one({edata.EVENTS: ObjectId(eid)})

    def test_hello(self):
        """ test trivial hello endpoint """
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.test_key, ret)

    def test_find_users(self):
        """ test if we can see the user collection within the database """
        find_users = ep.ListAllUsers(Resource)
        ret = find_users.get()
        # print("Found Users (Testing):", ret)
        self.assertNotEqual(len(ret), 0)

    def test_find_events(self):
        """ test if we can see the event collection within the database """
        find_events = ep.ListAllEvents(Resource)
        ret = find_events.get()
        # print("Found Users (Testing):", ret)
        self.assertNotEqual(len(ret), 0)

    def test_create_user(self):
        """
        See if we can successfully create a new user.
        Post-condition: user is in DB.
        """
        users = udata.get_all_users()
        self.assertIn(self.test_uid, users.keys())

    def test_create_event(self):
        """
        See if we can successfully create a new event.
        Post-condition: room is in DB.
        """
        events = edata.get_all_events()
        self.assertIn(self.test_eid, events.keys())
