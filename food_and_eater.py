# -*- coding: utf-8 -*-

class Eater:
    
    def eat(self, food):
        return Taste("food")

class Carnivore(Eater):
    
    def eat(self, food):
        return Taste(tasty=True)

class Food:
    pass

class Meat(Food):
    
    def __init__(self, name):
        self.__name = name

class Taste:

    def __init__(self, tasty):
        self.__tasty = tasty

    def __eq__(self, other):
        return self.__tasty == other.__tasty
