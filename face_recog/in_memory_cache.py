# ---- coding: utf-8 ----
# ===================================================
# Author: Gargi Mahale
# ===================================================
"""Description: Abstract class for handling data management in memory
 cache"""
# ===================================================
from abc import ABC, abstractmethod


class InMemoryCache(ABC):
    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def get_all_data(self):
        pass
