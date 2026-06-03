import pytest

from src.ingredient import Ingredient


class TestIngredient:
    def test_create_ingredient(self):
        ingredient = Ingredient("Мука", 500, "г")

        assert ingredient.name == "Мука"
        assert ingredient.quantity == 500.0
        assert ingredient.unit == "г"

    def test_str(self):
        ingredient = Ingredient("Мука", 500, "г")

        assert str(ingredient) == "Мука: 500.0 г"

    def test_quantity_must_be_plus(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", 0, "г")

    def test_equal_ingredients_with_same_name_and_unit(self):
        first = Ingredient("Мука", 500, "г")
        second = Ingredient("Мука", 200, "г")

        assert first == second

    def test_not_equal_ingredients_with_different_name(self):
        first = Ingredient("Мука", 500, "г")
        second = Ingredient("Сахар", 500, "г")

        assert first != second

    def test_not_equal_ingredients_with_different_unit(self):
        first = Ingredient("Мука", 500, "г")
        second = Ingredient("Мука", 500, "кг")

        assert first != second