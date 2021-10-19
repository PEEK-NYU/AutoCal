from unittest import TestCase, skip

import API.endpoints as endpoints


class EndpointTestCase(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_hellp(self):
        self.assertTrue(False)
        self.assertIn(ep.HELLO, ret)
