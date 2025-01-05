import re
from typing import List, Tuple


class Parser():

    def get_ingredients(self, input_text: List[str]) -> List[Tuple[int, int, int, int, int]]:
        """
        Example input:
            Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
        """
        ingredients = []

        for line in input_text:
            m = re.match(r'\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
            capacity, durability, flavor, texture, calories = map(int, m.groups())
            ingredients.append((capacity, durability, flavor, texture, calories))

        return ingredients
