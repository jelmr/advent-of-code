from typing import List

from solution import Solution
from year_2015.day_11.solver import Solver


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        solver = Solver()
        pw1 = solver.solve(input_text[0])
        pw2 = solver.solve(pw1)
        return pw2
