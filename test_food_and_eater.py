# -*- coding: utf-8 -*-

from taste import Taste
from eater import Eater, Carnivore, Vegetarian
from food import Food, Meat, Vegetable

def test():
    assert Eater().eat(Food("food")) == Taste()
    assert Carnivore().eat(Meat("Steak")) == Taste(tasty=True)
    assert Carnivore().eat(Vegetable("Salad")) == Taste(tasty=False)
    assert Vegetarian().eat(Vegetable("salad")) == Taste(tasty=True)
    assert Vegetarian().eat(Meat("Steak")) == Taste(tasty=False)
