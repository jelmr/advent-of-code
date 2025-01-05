from typing import List

import numpy as np

from solution import Solution
from year_2015.day_18.parser import Parser
from year_2015.day_18.game_of_life import GameOfLife


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        return self.run_generations(input_text, 100)

    def run_generations(self, input_text: List[str], generations: int) -> str | int:
        matrix = Parser().get_matrix(input_text)
        broken_lights = self.get_broken_lights(matrix)
        matrix[broken_lights == 1] = 1

        game_of_live = GameOfLife()
        for i in range(generations):
            matrix = game_of_live.iterate(matrix)
            matrix[broken_lights == 1] = 1

        return int(np.sum(matrix))

    def get_broken_lights(self, matrix: np.array) -> np.array:
        width = matrix.shape[0]
        broken_lights = np.zeros(matrix.shape, dtype=np.int64)
        coords = [(0, 0), (width-1, 0), (0, width-1), (width-1, width-1)]
        broken_lights[*zip(*coords)] = 1
        return broken_lights
