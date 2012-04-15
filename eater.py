# -*- coding: utf-8 -*-

from taste import Taste

class Eater:
    
    def eat(self, food):
        return food.is_eaten_by(self)


class Carnivore(Eater):
    pass


class Vegetarian(Eater):
    pass
