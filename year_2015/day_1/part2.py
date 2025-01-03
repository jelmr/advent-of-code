from typing import List

from solution import Solution


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        idx = 1
        floor = 0
        for c in input_text[0].strip():
            floor += 1 if c == '(' else -1
            if floor == -1:
                return idx
            idx += 1
