# -*- coding: utf-8 -*-

from food_and_eater import Eater, Food, Taste, Carnivore, Meat, Vegetable

def test():
    assert Eater().eat(Food("food")) == Taste()
    assert Carnivore().eat(Meat("Steak")) == Taste(tasty=True)
    assert Carnivore().eat(Vegetable("Salad")) == Taste(tasty=False)
