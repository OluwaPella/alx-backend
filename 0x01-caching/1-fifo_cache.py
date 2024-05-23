#!/usr/bin/python3
from base_caching import BaseCaching
from collections import deque

class FIFOCache( BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key  or item:
             self.cache_data[key] = item
        if len(self.cache_data) >  BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
        self.cache_data[key] = item
    def get(self, key):
        return self.cache_data.get(key, None)




    