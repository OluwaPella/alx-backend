#!/usr/bin/python3
from base_caching import BaseCaching
from collections import OrderedDict 

class FIFOCache( BaseCaching):
    """ FIFOCache defines"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key  is None or item is None:
             self.cache_data[key] = item
        if len(self.cache_data) >  BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD: {}".format(first_key))
    def get(self, key):
        """ Get an item by key"""
        return self.cache_data.get(key, None)




    