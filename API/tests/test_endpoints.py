from unittest import TestCase, skip
from flask_restx import Resource, Api
import random

import API.endpoints as endpoints
import db.data as db



class EndpointTestCase(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_hello(self):
        self.assertTrue(False)
#        self.assertIn(ep.HELLO, ret)
