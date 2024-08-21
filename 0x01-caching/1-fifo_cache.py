#!/usr/bin/env python3
"""task 1.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that_
    """
    def __init__(self):
        """Initializes init method.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns the item value to the key in the dictionary.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves.
        """
        return self.cache_data.get(key, None)
