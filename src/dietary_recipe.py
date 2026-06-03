from src.recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, title, ingredients, diet_type):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        scaled_recipe = super().scale(ratio)

        new_recipe = DietaryRecipe(
            scaled_recipe.title,
            scaled_recipe.ingredients,
            self.diet_type
        )

        return new_recipe

    def __str__(self):
        result = "Диетический рецепт: " + self.title + "\n"
        result = result + "Тип диеты: " + self.diet_type + "\n"

        for ingredient in self.ingredients:
            result = result + "- " + str(ingredient) + "\n"

        return result