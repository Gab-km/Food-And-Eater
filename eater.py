# -*- coding: utf-8 -*-

from taste import Taste

class Eater:
    
    def eat(self, food):
        return Taste()


class Carnivore(Eater):
    
    def eat(self, food):
        return food.is_eaten_by(self)


class Vegetarian(Eater):

    def eat(self, food):
        return food.is_eaten_by(self)
