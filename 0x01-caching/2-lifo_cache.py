#!/usr/bin/env python3
""" LIFO Caching
"""
from collections import deque
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFO Caching
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.order.pop()
            print("DISCARD:", last_key)
        self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)