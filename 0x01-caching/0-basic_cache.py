from base_caching import BaseCaching 


class BasicCachea(BaseCaching):
    def __init__(self):
        self.cache_data = {}


    def put(self, key, item):
        """ Add an item in the cache"""
        self.cache_data[key] = item
        if key is None or item is None:
            return None
        
    def get(self, key):
        """ Get an item by key and return it's value
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
    
