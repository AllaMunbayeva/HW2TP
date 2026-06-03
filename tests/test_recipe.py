from src.ingredient import Ingredient
from src.recipe import Recipe


class TestRecipe:
    def test_create_recipe(self):
        flour = Ingredient("Мука", 500, "г")
        milk = Ingredient("Молоко", 200, "мл")

        recipe = Recipe("Блины", [flour, milk])

        assert recipe.title == "Блины"
        assert recipe.ingredients[0] == flour
        assert recipe.ingredients[1] == milk

    def test_add_new_ingredient(self):
        flour = Ingredient("Мука", 500, "г")
        milk = Ingredient("Молоко", 200, "мл")

        recipe = Recipe("Блины", [flour])
        recipe.add_ingredient(milk)

        assert len(recipe) == 2
        assert recipe.ingredients[1] == milk

    def test_add_same_ingredient_sum_quantity(self):
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 200, "г")

        recipe = Recipe("Блины", [flour1])
        recipe.add_ingredient(flour2)

        assert len(recipe) == 1
        assert recipe.ingredients[0].name == "Мука"
        assert recipe.ingredients[0].quantity == 700.0
        assert recipe.ingredients[0].unit == "г"

    def test_is_valid_ratio_true_for_plus(self):
        result = Recipe.is_valid_ratio(2)

        assert result is True

    def test_is_valid_ratio_true_for_plus_float(self):
        result = Recipe.is_valid_ratio(0.5)

        assert result is True

    def test_is_valid_ratio_false_for_zero(self):
        result = Recipe.is_valid_ratio(0)

        assert result is False

    def test_is_valid_ratio_false_for_minus(self):
        result = Recipe.is_valid_ratio(-1)

        assert result is False


    def test_scale_recipe(self):
        flour = Ingredient("Мука", 500, "г")
        milk = Ingredient("Молоко", 200, "мл")

        recipe = Recipe("Блины", [flour, milk])
        new_recipe = recipe.scale(2)

        assert new_recipe.title == "Блины"
        assert new_recipe.ingredients[0].quantity == 1000.0
        assert new_recipe.ingredients[1].quantity == 400.0

    def test_scale_does_not_change_old_recipe(self):
        flour = Ingredient("Мука", 500, "г")

        recipe = Recipe("Блины", [flour])
        new_recipe = recipe.scale(2)

        assert recipe.ingredients[0].quantity == 500.0
        assert new_recipe.ingredients[0].quantity == 1000.0

    def test_len_returns_unique_ingredients_count(self):
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 200, "г")
        milk = Ingredient("Молоко", 200, "мл")

        recipe = Recipe("Блины", [flour1, flour2, milk])

        assert len(recipe) == 2

    def test_str_contains_title_and_ingredients(self):
        flour = Ingredient("Мука", 500, "г")

        recipe = Recipe("Блины", [flour])
        result = str(recipe)

        assert "Блины" in result
        assert "Мука" in result
        assert "500.0" in result
        assert "г" in result