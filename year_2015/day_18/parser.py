from typing import List

import numpy as np


class Parser:
    def get_matrix(self, lines: List[str]) -> np.array:
        grid = [
            [1 if char == '#' else 0 for char in line]
            for line in lines
        ]

        return np.array(grid, dtype=np.int64)