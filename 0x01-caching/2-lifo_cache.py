#!/usr/bin/env python3
""" LIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFO Caching
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            remove_key = (self.cache_data.keys())[-1]
            self.cache_data .pop(remove_key)
            print("DISCARD:", remove_key)
        self.cache_data[key] = item 

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)