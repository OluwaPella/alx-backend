#!/usr/bin/python3
""" LRU Caching"""
from base_caching import BaseCaching


class LRUCache (BaseCaching):
    """ LRU Caching"""
    def __init__(self):
        """
        Initiliaze"""
        super().__init__()

    def put(self, key, item):
        self.cache_data = item
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed = list(self.cache_data.keys())[-1]
            self.cache_data.pop(removed)
            print("DISCARD: {}".format(removed))
        

    def get(self, key):
        return self.cache_data(key)