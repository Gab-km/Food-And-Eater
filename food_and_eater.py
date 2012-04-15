# -*- coding: utf-8 -*-

class Eater:
    
    def eat(self, food):
        return Taste("food")

class Food:
    pass

class Taste:

    def __init__(self, name):
        self.__name = name
