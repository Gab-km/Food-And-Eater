# -*- coding: utf-8 -*-

from food_and_eater import Eater, Food, Taste

def test():
    assert Eater().eat(Food()) == Taste()
