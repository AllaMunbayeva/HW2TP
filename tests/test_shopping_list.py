import pytest

from src.ingredient import Ingredient
from src.recipe import Recipe
from src.shopping_list import ShoppingList


class TestShoppingList:
    def test_add_recipe(self):
        flour = Ingredient("Мука", 500, "г")
        recipe = Recipe("Блины", [flour])

        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 2)

        result = shopping_list.get_list()

        assert len(result) == 1
        assert result[0].name == "Мука"
        assert result[0].quantity == 1000.0
        assert result[0].unit == "г"

    def test_add_recipe_with_zero_portions(self):
        flour = Ingredient("Мука", 500, "г")
        recipe = Recipe("Блины", [flour])

        shopping_list = ShoppingList()

        with pytest.raises(ValueError):
            shopping_list.add_recipe(recipe, 0)

    def test_remove_recipe(self):
        flour = Ingredient("Мука", 500, "г")
        recipe = Recipe("Блины", [flour])

        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 1)
        shopping_list.remove_recipe("Блины")

        result = shopping_list.get_list()

        assert result == []

    def test_remove_unknown_recipe_does_nothing(self):
        flour = Ingredient("Мука", 500, "г")
        recipe = Recipe("Блины", [flour])

        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 1)
        shopping_list.remove_recipe("Пицца")

        result = shopping_list.get_list()

        assert len(result) == 1
        assert result[0].name == "Мука"
        assert result[0].quantity == 500.0

    def test_get_list_sum_same_ingredients(self):
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 200, "г")

        first_recipe = Recipe("Блины", [flour1])
        second_recipe = Recipe("Пирог", [flour2])

        shopping_list = ShoppingList()
        shopping_list.add_recipe(first_recipe, 1)
        shopping_list.add_recipe(second_recipe, 1)

        result = shopping_list.get_list()

        assert len(result) == 1
        assert result[0].name == "Мука"
        assert result[0].quantity == 700.0
        assert result[0].unit == "г"

    def test_get_list_sorts_by_ingredient_name(self):
        sugar = Ingredient("Сахар", 100, "г")
        flour = Ingredient("Мука", 500, "г")

        recipe = Recipe("Блины", [sugar, flour])

        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 1)

        result = shopping_list.get_list()

        assert result[0].name == "Мука"
        assert result[1].name == "Сахар"

    def test_add_shopping_lists(self):
        flour = Ingredient("Мука", 500, "г")
        milk = Ingredient("Молоко", 200, "мл")

        first_recipe = Recipe("Блины", [flour])
        second_recipe = Recipe("Каша", [milk])

        first_list = ShoppingList()
        second_list = ShoppingList()

        first_list.add_recipe(first_recipe, 1)
        second_list.add_recipe(second_recipe, 1)

        result_list = first_list + second_list
        result = result_list.get_list()

        assert len(result) == 2