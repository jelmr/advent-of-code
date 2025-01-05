from typing import List

from solution import Solution
from year_2015.day_17.solver import Solver


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        containers = list(map(int, input_text))
        count, _ =  Solver().combinations(containers, 150)
        return count
