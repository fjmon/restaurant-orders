import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction
    )


def test_dish():
    pizza = Dish("pizza", 14.50)
    muqueca_camarao = Dish('muqueca_camarao', 35.00)
    pizza.add_ingredient_dependency(Ingredient('queijo mussarela'), 5)

    assert pizza.name == 'pizza'
    assert pizza == pizza
    assert hash(pizza) == hash(repr(pizza))
    assert pizza != muqueca_camarao
    assert repr(pizza) == "Dish('pizza', R$14.50)"
    assert pizza.get_ingredients() == {Ingredient('queijo mussarela')}
    assert pizza.get_restrictions() == {
        Restriction.ANIMAL_DERIVED, Restriction.LACTOSE
        }

    with pytest.raises(TypeError):
        Dish('name', 'price')
    with pytest.raises(ValueError):
        Dish('name', 0)
