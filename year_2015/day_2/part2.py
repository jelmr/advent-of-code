from typing import List

from solution import Solution


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        total = 0
        for dimensions in input_text:
            l, w, h = map(int, dimensions.split('x'))
            wrap = 2 * l + 2 * w + 2 * h - 2 * max(l, w, h)
            ribbon = l * w * h
            total += wrap + ribbon
        return total
