from itertools import permutations
from typing import List, Tuple

from solution import Solution
from year_2015.day_13.parser import Parser
from year_2015.day_13.solver import Solver


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        happiness_matrix = Parser().get_happiness_matrix(input_text)
        return Solver().solve(happiness_matrix)
