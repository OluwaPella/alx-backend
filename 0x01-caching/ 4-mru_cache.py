#!/usr/bin/python3
"""MRUCache
"""

from base_caching import BaseCaching
from collections import OrderedDict

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
        
    def get(self, key):
        """getting data from cache using the key"""
        return self.cache_data(key)