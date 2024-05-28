#!/usr/bin/python3
""" LRU Caching"""
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
            discard_key = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(discard_key))
            self.cache_data[key] = item
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        

    def get(self, key):
        """ Get an item by key"""
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data(key)
        return None