#!/usr/bin/env python3
""" FIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):

    """represents a caching system"""
    def __init__(self):
        """ Initiliaze the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) >  BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)

            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
    
