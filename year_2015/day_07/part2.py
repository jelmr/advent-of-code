from typing import List

from solution import Solution
from year_2015.day_07.solver import Solver


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        a = Solver({}).solve(input_text)
        return Solver({'b': a}).solve(input_text)
