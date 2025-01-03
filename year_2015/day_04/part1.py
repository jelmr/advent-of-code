from typing import List

from solution import Solution
from year_2015.day_04.hash_finder import HashFinder


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        return HashFinder(input_text).solve('00000')
