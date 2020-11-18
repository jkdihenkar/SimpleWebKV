import unittest

import simplekv_server

class TestSimpleKVServer(unittest.TestCase):

    def setUp(self):
        self.app = simplekv_server.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_content(self):
        expected = "Hello from SimpleKV"
        response = self.app.get('/')
        # print(dir(response))
        self.assertEqual(response.data.decode('utf-8'), expected)