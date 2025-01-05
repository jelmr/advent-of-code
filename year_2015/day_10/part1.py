from typing import List

from solution import Solution
from year_2015.day_10.solver import Solver


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        return Solver().steps(input_text[0], 40)
