# -*- coding: utf-8 -*-

from taste import Taste

class Eater:
    
    def eat(self, food):
        return Taste()

class Carnivore(Eater):
    
    def eat(self, food):
        if isinstance(food, Meat):
            return Taste(tasty=True)
        else:
            return Taste(tasty=False)

class Vegetarian(Eater):

    def eat(self, food):
        return Taste(tasty=True)
