from itertools import product
from typing import List

from solution import Solution
from year_2015.day_15.parser import Parser


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        ingredients = Parser().get_ingredients(input_text)

        combinations = product(range(0, 101), repeat=len(ingredients))
        valid_combinations = [comb for comb in combinations if sum(comb) == 100]

        def get_score(combination):
            capacity, durability, flavor, texture = 0, 0, 0, 0
            for times, ingredient in zip(combination, ingredients):
                ingredient_capacity, ingredient_durability, ingredient_flavor, ingredient_texture, _ = ingredient
                capacity += times * ingredient_capacity
                durability += times * ingredient_durability
                flavor += times * ingredient_flavor
                texture += times * ingredient_texture
            return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

        return max(get_score(combination) for combination in valid_combinations)
