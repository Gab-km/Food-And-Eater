# -*- coding: utf-8 -*-

class Taste:

    def __init__(self, tasty=True):
        self.__tasty = tasty

    def __eq__(self, other):
        return self.__tasty == other.__tasty
