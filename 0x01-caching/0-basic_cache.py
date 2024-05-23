#!/usr/bin/python3
from base_caching import BaseCaching

class BasicCache(BaseCaching):

    def put(self, key, item):
        """ Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
        
    def get(self, key):
        """ Get an item by key and return it's value
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
    
