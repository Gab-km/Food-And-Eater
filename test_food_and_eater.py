# -*- coding: utf-8 -*-

from food_and_eater import Eater, Food, Taste, Carnivore, Meat

def test():
    assert Eater().eat(Food()) == Taste("food")
    assert Carnivore().eat(Meat("Steak")) == Taste(tasty=True)
