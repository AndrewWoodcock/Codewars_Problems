class Recipe:

    def __init__(self, ingredients: dict):
        self.ingredients = ingredients


class Stock:

    def __init__(self, my_ingredients: dict):
        self.my_ingredients = my_ingredients


def review_recipe(recipe: Recipe, available: Stock) -> int:
    cake_count = None
    for ingredient, measure in recipe.ingredients.items():
        if ingredient not in available.my_ingredients:
            return 0
        else:
            req_measure = measure
            stock_measure = available.my_ingredients[ingredient]
            possible = int(stock_measure / req_measure)
            if cake_count is None:
                cake_count = possible
            elif possible < cake_count:
                cake_count = possible
    return cake_count


def cakes(recipe, available):
    recipe = Recipe(recipe)
    stock = Stock(available)
    return review_recipe(recipe, stock)


print(cakes({'milk': 51, 'eggs': 98, 'flour': 77},
            {'flour': 6322, 'eggs': 4, 'butter': 5138, 'oil': 7238, 'apples': 6657, 'crumbles': 8932, 'cream': 6734,
             'pears': 5367, 'nuts': 586, 'chocolate': 991, 'milk': 7730, 'sugar': 7295, 'cocoa': 3367}))
