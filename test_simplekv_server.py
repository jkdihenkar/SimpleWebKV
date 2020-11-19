"""
Test SimpleKV Server
"""

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

    def test_put_endpoint_success(self):
        response = self.app.put("/put/teststore", data='{"arg1":"val1"}')
        self.assertEqual(response.data.decode('utf-8'), '{"result":"success"}\n')

    def test_put_endpoint_baddata(self):
        response = self.app.put("/put/teststore", data='{"arg1............')
        self.assertEqual(response.status_code, 400)

    def test_get_endpoint_success(self):
        response = self.app.put("/put/teststore", data='{"arg1":"val1"}')
        response = self.app.get("/get/teststore/arg1")
        self.assertEqual(response.data.decode('utf-8'), '{"result":"val1"}\n')

    def test_get_endpoint_notfound(self):
        response = self.app.put("/put/teststore", data='{"arg1":"val1"}')
        response = self.app.get("/get/teststore/arg2")
        self.assertEqual(response.data.decode('utf-8'), '{"result":"not_found"}\n')

        
