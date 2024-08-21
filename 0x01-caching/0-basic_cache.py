#!/usr/bin/env python3
"""Module for task 0.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system that inherits from BaseCaching.
    """
    def put(self, key, item):
        """Assigns the item valu
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """def get
        """
        return self.cache_data.get(key, None)
