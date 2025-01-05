from typing import List

from solution import Solution
from year_2015.day_13.parser import Parser
from year_2015.day_13.solver import Solver


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        happiness_matrix = Parser().get_happiness_matrix(input_text)
        # Add yourself to the matrix
        happiness_matrix = [row + [0] for row in happiness_matrix] + [[0] * len(happiness_matrix)]
        return Solver().solve(happiness_matrix)
