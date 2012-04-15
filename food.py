# -*- coding: utf-8 -*-

from eater import Carnivore
from taste import Taste

class Food:

    def __init__(self, name):
        self.__name = name

    def is_eaten_by(self, eater):
        pass

class Meat(Food):
    
    def is_eaten_by(self, eater):
        if isinstance(eater, Carnivore):
            return Taste(tasty=True)
        else:
            return Taste(tasty=False)

class Vegetable(Food):
    
    def is_eaten_by(self, eater):
        if isinstance(eater, Vegetarian):
            return Taste(tasty=True)
        else:
            return Taste(tasty=False)

