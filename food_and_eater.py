# -*- coding: utf-8 -*-

class Eater:
    
    def eat(self, food):
        return Taste("food")

class Carnivore(Eater):
    pass

class Food:
    pass

class Meat(Food):
    
    def __init__(self, name):
        self.__name = name

class Taste:

    def __init__(self, name):
        self.__name = name

    def __eq__(self, other):
        return self.__name == other.__name
