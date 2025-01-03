from typing import List

from solution import Solution


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        return sum(1 if c == '(' else -1 for c in input_text[0].strip())
