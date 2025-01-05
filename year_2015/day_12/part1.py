import re
from typing import List

from solution import Solution


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        return sum(map(int, re.findall(r'(-?\d+)', input_text[0])))
