# -*- coding: utf-8 -*-

from taste import Taste
from food import Meat, Vegetable

class Eater:
    
    def eat(self, food):
        return Taste()

class Carnivore(Eater):
    
    def eat(self, food):
        food.is_eaten_by(self)


class Vegetarian(Eater):

    def eat(self, food):
        if isinstance(food, Vegetable):
            return Taste(tasty=True)
        else:
            return Taste(tasty=False)
