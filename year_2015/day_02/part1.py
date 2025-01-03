from typing import List

from solution import Solution


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        total = 0
        for dimensions in input_text:
            l, w, h = map(int, dimensions.split('x'))
            a = l * w
            b = w * h
            c = h * l
            total += 2 * a + 2 * b + 2 * c + min(a, b, c)
        return total
