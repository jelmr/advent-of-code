from typing import List

from solution import Solution
from year_2015.day_14.parser import Parser
from year_2015.day_14.solver import Solver


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        reindeers = Parser().get_reindeers(input_text)
        return Solver().calculate_score(reindeers, 2503)
