from unittest import TestCase, skip
from flask_restx import Resource, Api
import random

import API.endpoints as ep
import db.data as db

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

    def test_create_user(self):
        """
        See if we can successfully create a new user.
        Post-condition: user is in DB.
        """
        cu = ep.CreateUser(Resource)
        new_user = new_entity_name("user")
        ret = cu.post(new_user)
        users = db.get_users()
        self.assertIn(new_user, users)
        
       
    def test_delete_user(self):
        """
        See if we can successfully delete a user.
        Post-condition: user no longer in DB.
        """
        usrname = "delete_test_user"
        db.add_user(usrname);
        ret = ep.DeleteUser(Resource).post(usrname)
        users = db.get_users()
        self.assertFalse((usrname in users))
 
        
    def test_list_users(self):
        """
        See if we can successfully list all users.
        Post-condition: nothing changes.
        """
        ret = ep.GetUsers(Resource).get()
        users = db.get_users()
        msg = "test_list_users: Error, returned users aren't equivalent to databse users"
        self.assertEqual(ret, users, msg)

    def test_create_event(self):
        """
        See if we can successfully create a new event.
        Post-condition: event is in DB.
        """
        cr = ep.CreateEvent(Resource)
        new_event = new_entity_name("event")
        ret = cr.post(new_event, "test_user")
        events = db.get_events()
        self.assertIn(ret['id'], events)


    def test_delete_event(self):
        """
        See if we can successfully delete a event.
        Post-condition: event no longer in DB.
        """
        event = db.add_event("testEvent", "testLoc", 1640146943, 1640146943, "test descr", "Paul", ["Paul"])
        ret = ep.DeleteEvent(Resource).post(event['id'])
        events = db.get_events()
        self.assertFalse((event['id'] in events))      
        
    def test_list_events(self):
        """
        See if we can successfully list all events.
        Post-condition: noting changes.
        """
        ret = ep.ListEvents(Resource).get()
        events = db.get_events()
        msg = "test_list_events: Error, returned events aren't equivalent to databse events"
        self.assertEqual(ret, events, msg)


    def test1_event(self):
        """
        Post-condition 1: return is a dictionary.
        """
        lr = ep.ListEvents(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, dict)

    def test2_event(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        lr = ep.ListEvents(Resource)
        ret = lr.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test3_event(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        lr = ep.ListEvents(Resource)
        ret = lr.get()
        for val in ret.values():
            self.assertIsInstance(val, dict)
