#!/usr/bin/python3
from base_caching import BaseCaching

class BasicCache(BaseCaching):

    def put(self, key, item):
        """ Add an item in the cache"""
        self.cache_data[key] = item
        if key is None or item is None:
            return None
        
    def get(self, key):
        """ Get an item by key and return it's value
        """
        return self.cache_data.get(key, None)
    
