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


if __name__ == "__main__":
    unittest.main()
