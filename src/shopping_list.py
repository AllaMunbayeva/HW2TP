from src.ingredient import Ingredient
from src.recipe import Recipe


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            item = (ingredient, recipe.title)
            self._items.append(item)

    def remove_recipe(self, title: str):
        new_items = []

        for item in self._items:
            recipe_title = item[1]

            if recipe_title != title:
                new_items.append(item)

        self._items = new_items

    def get_list(self):
        result = {}

        for item in self._items:
            ingredient = item[0]

            key = (ingredient.name, ingredient.unit)

            if key in result:
                result[key] = result[key] + ingredient.quantity
            else:
                result[key] = ingredient.quantity

        shopping_list = []

        for key in result:
            name = key[0]
            unit = key[1]
            quantity = result[key]

            ingredient = Ingredient(name, quantity, unit)
            shopping_list.append(ingredient)

        def get_ingredient_name(ingredient):
            return ingredient.name

        shopping_list.sort(key=get_ingredient_name)

        return shopping_list

    def __add__(self, other):
        new_shopping_list = ShoppingList()

        for item in self._items:
            new_shopping_list._items.append(item)

        for item in other._items:
            new_shopping_list._items.append(item)

        return new_shopping_list