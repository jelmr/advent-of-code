from typing import List, Tuple

from solution import Solution
from year_2015.day_14.parser import Parser
from year_2015.day_14.solver import Solver


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        reindeers = Parser().get_reindeers(input_text)
        return max(Solver().calculate_distance(reindeer, 2503) for reindeer in reindeers)
