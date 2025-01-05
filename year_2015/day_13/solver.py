from itertools import permutations
from typing import List


class Solver:
    def solve(self, happiness_matrix: List[List[int]]) -> int:
        seating_permutations = permutations(list(range(len(happiness_matrix))))

        def evaluate(permutation) -> int:
            happiness_change = 0

            for idx, person_id in enumerate(permutation):
                left_idx = len(permutation) - 1 if idx == 0 else idx - 1
                happiness_change += happiness_matrix[person_id][permutation[left_idx]]
                right_idx = 0 if idx == len(permutation) - 1 else idx + 1
                happiness_change += happiness_matrix[person_id][permutation[right_idx]]

            return happiness_change

        return max(evaluate(permutation) for permutation in list(seating_permutations))
