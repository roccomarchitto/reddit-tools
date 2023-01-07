#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
TODO
"""

from abc import ABC, abstractmethod


class DatabaseWrapper(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    # TODO - should this be an abstractclassmethod?
    @abstractmethod
    def submit_post(self):
        pass


class MongoWrapper(DatabaseWrapper):
    def __init__(self):
        pass

    def submit_post(self):
        pass
