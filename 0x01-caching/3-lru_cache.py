#!/usr/bin/python3
""" LRU Caching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache (BaseCaching):
    """ LRU Caching"""
    def __init__(self):
        """
        Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data.get(key, None)
        