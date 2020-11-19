"""
SimpleKV Core Utilities
"""

import logging


class SimpleKV:
    """
    SimpleKV - Core Utils for a Simple Key Value Store
    """

    storedict = {}

    def __init__(self, storedict={}):
        """
        Init the storedict as empty or from a predefined dict.
        """
        self.storedict = storedict

    def get(self, key):
        """
        Get a key from store.
        """
        if key in self.storedict:
            return self.storedict.get(key)
        return False

    def exists(self, key):
        """
        Check if key exists in the store.
        """
        if key in self.storedict:
            return True
        return False

    def put(self, key, val):
        """
        Put a key-value in store
        """
        try:
            self.storedict[key] = val
            return True
        except Exception as e:
            logging.exception("Cannot set %s:%s; Exception: %s", key, val, e)
            return False
