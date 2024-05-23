#!/usr/bin/python3
from base_caching import BaseCaching

class FIFOCache( BaseCaching):
    def __init__(self):

        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) >  BaseCaching.MAX_ITEMS:
            if hasattr(self.cache_data, 'keys'):
                first_key = list(self.cache_data.keys())[0]
            else:
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

    def get(self, key):
        return self.cache_data.get(key, None)




    