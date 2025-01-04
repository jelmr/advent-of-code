from typing import List

from algorithms.held_karp.held_karp import HeldKarp
from solution import Solution
from year_2015.day_09.parser import Parser


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        dist = Parser().get_distance_matrix(input_text)
        return HeldKarp(fixed_start=False, back_to_start=False).best_total_distance(dist)
