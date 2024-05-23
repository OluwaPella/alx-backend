#!/usr/bin/python3
""" BaseCache module.
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines"""
    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item 
    def get(self, key):
        """ Get an item """
        return self.cache_data.get(key, None)
