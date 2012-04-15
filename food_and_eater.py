# -*- coding: utf-8 -*-

class Eater:
    
    def eat(self, food):
        return Taste()

class Carnivore(Eater):
    
    def eat(self, food):
        if isinstance(food, Meat):
            return Taste(tasty=True)
        else:
            return Taste(tasty=False)

class Food:

    def __init__(self, name):
        self.__name = name

class Meat(Food):
    pass
    
class Vegetable(Food):
    pass    

class Taste:

    def __init__(self, tasty=True):
        self.__tasty = tasty

    def __eq__(self, other):
        return self.__tasty == other.__tasty
