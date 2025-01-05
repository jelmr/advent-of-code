from typing import List

from solution import Solution
from year_2015.day_17.solver import Solver


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        containers = list(map(int, input_text))
        solver = Solver()

        _, least_containers = solver.combinations(containers, 150)
        count, _ = solver.combinations(containers, 150, allowed_containers=least_containers)

        return count
