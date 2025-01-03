from typing import List

import numpy as np

from solution import Solution
from year_2015.day_06.parser import Parser


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        grid = np.zeros((1000, 1000), dtype=int)

        for action, (x1, y1), (x2, y2) in Parser(input_text).get_instructions():
            match action:
                case 'turn on':
                    grid[x1:x2 + 1, y1:y2 + 1] += 1
                case 'turn off':
                    grid[x1:x2 + 1, y1:y2 + 1] = np.maximum(grid[x1:x2 + 1, y1:y2 + 1] - 1, 0)
                case 'toggle':
                    grid[x1:x2 + 1, y1:y2 + 1] += 2

        return int(np.sum(grid))
