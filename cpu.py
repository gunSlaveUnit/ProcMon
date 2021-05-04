"""
Made by Aleksander Tyamin
04.05.2021
"""

import psutil


class CPU:
    def __init__(self):
        self.__amount_cores = psutil.cpu_count(logical=False)
        self.__amount_threads = psutil.cpu_count()

    @property
    def amount_cores(self):
        return self.__amount_cores

    @property
    def amount_threads(self):
        return self.__amount_threads

    @property
    def cores_loading(self):
        return psutil.cpu_percent(percpu=True)
