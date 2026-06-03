from src.ingredient import Ingredient


class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = []

        for ingredient in ingredients:
            self.add_ingredient(ingredient)

    def add_ingredient(self, ingredient):
        for item in self.ingredients:
            if item == ingredient:
                item.quantity = item.quantity + ingredient.quantity
                return

        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, int):
            return ratio > 0

        if isinstance(ratio, float):
            return ratio > 0

        return False

    def scale(self, ratio):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")

        new_ingredients = []

        for ingredient in self.ingredients:
            new_quantity = ingredient.quantity * ratio

            new_ingredient = Ingredient(
                ingredient.name,
                new_quantity,
                ingredient.unit
            )

            new_ingredients.append(new_ingredient)

        new_recipe = Recipe(self.title, new_ingredients)

        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = "Рецепт: " + self.title + "\n"

        for ingredient in self.ingredients:
            result = result + "- " + str(ingredient) + "\n"

        return result