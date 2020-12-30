"""
Test SimpleKV Core Utils
"""

import unittest

from simplekv import SimpleKV

class TestSimpleKV(unittest.TestCase):

    test_kv = {'hello': 'world'}
    simple_kv_store = None

    def setUp(self):
        self.simple_kv_store = SimpleKV(self.test_kv)

    def test_simplekv_get(self):
        self.assertEqual(self.simple_kv_store.get('hello'), 'world')

    def test_simplekv_put(self):
        self.assertTrue(self.simple_kv_store.put('something', 'nothing'))

    def test_simplekv_except(self):
        with self.assertRaises(Exception) as raisetest:
            self.simple_kv_store.put(1/0, 'hi') # HAHA...

    def test_simplekv_exists(self):
        self.assertTrue(self.simple_kv_store.exists('hello'))

    def test_simplekv_notexists(self):
        self.assertFalse(self.simple_kv_store.exists('nothello'))

    def test_simplekv_keynotfound(self):
        self.assertFalse(self.simple_kv_store.get('nothello'))

    def test_simplekv_get_oneisone(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
