from src.models.ingredient import (
    Ingredient, Restriction
    )  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ing_1 = Ingredient('manteiga')
    ing_2 = Ingredient('carne')
    ing_3 = Ingredient('manteiga')

    assert ing_1._repr_() == "Ingredient('manteiga')"
    assert ing_1._hash() == ing_3.hash_()
    assert ing_1._hash() != ing_2.hash_()

    assert ing_1.name == 'manteiga'
    assert ing_2.name != 'frango'
    assert ing_1._eq_(ing_3)

    assert ing_1.restrictions == {Restriction.LACTOSE,
                                  Restriction.ANIMAL_DERIVED}
