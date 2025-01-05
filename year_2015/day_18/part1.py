from typing import List

import numpy as np

from solution import Solution
from year_2015.day_18.game_of_life import GameOfLife
from year_2015.day_18.parser import Parser


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        return self.run_generations(input_text, 100)

    def run_generations(self, input_text: List[str], generations: int) -> str | int:
        game_of_live = GameOfLife()
        matrix = Parser().get_matrix(input_text)
        for i in range(generations):
            matrix = game_of_live.iterate(matrix)

        return int(np.sum(matrix))
