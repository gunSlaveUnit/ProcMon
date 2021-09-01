"""
Made by Aleksander Tyamin
04.05.2021
"""

import psutil


class RAM:
    @property
    def memory_usage(self):
        """Return statistics about system memory usage as a namedtuple"""
        return psutil.virtual_memory()
