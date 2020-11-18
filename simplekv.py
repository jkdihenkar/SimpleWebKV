import logging


class SimpleKV:

    storedict = {}

    def __init__(self, storedict={}):
        self.storedict = storedict

    def get(self, key):
        return self.storedict.get(key, None)

    def put(self, key, val):
        try:
            self.storedict[key] = val
            return True
        except Exception as e:
            logging.exception("Cannot set {}:{}; Exception: {}".format(key, val, e))
            return False
