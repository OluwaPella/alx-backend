#!/usr/bin/python3
"""MRUCache
"""
from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()


    def put(self, key, item):
        """ adding item to cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.cache_data.popitem(key, last=False)
            print("DISCARD", mru_key)
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

        
    def get(self, key):
        """getting data from cache using the key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data(key, None)