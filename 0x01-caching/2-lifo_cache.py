#!/usr/bin/python3
""" doc doc doc """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """doc doc doc"""

    def __init__(self):
        """doc doc doc"""
        super().__init__()

    def put(self, key, item):
        """doc doc doc"""
        if key  and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed_key)
                print("DISCARD: {}".format(removed_key))
            self.cache_data[key] = item

    def get(self, key):
        """doc doc doc"""
        return self.cache_data.get(key)