import sys
from functools import cache
from typing import List

from solution import Solution


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        def get_stats(mask):
            packages = 0
            quantum = 1
            idx = 0
            while mask:
                if mask & 1:
                    quantum *= weights[idx]
                    packages += 1
                idx += 1
                mask >>= 1
            return packages, quantum

        def store_new_best(mask1):
            nonlocal fewest_packages, best_quantum
            packages, quantum = get_stats(mask1)

            fewest_packages = min(fewest_packages, packages)
            if packages == fewest_packages:
                best_quantum = min(best_quantum, quantum)

            solved.add(mask1)

        def explore(available, start_idx, mask1, weight1, mask2, weight2):
            if mask1 in solved:
                return  # The distribution of packages in group 2/3 doesn't matter, so we abandon this branch
            if weight1 == desired:
                packages, quantum = get_stats(mask1)
                if packages > fewest_packages or (packages == fewest_packages and quantum > best_quantum):
                    return  # We have already seen a better group 1, so we abandon this branch

            if weight1 == desired and weight2 == desired:
                store_new_best(mask1)

            try_mask = available & ~mask1

            idx = start_idx
            try_mask >>= idx

            while try_mask:
                if try_mask & 1:
                    weight = weights[idx]
                    new_available = available & ~(1 << idx)  # unset idx, it's been used

                    if weight1 == desired:  # G1 done, try filling G2
                        if weight2 + weight <= desired:
                            start_idx = 0 if weight2 + weight == desired else idx + 1
                            explore(new_available, start_idx, mask1, weight1, mask2 | 1 << idx, weight2 + weight)
                    else:  # Try to fill G1
                        if weight1 + weight <= desired:
                            start_idx = 0 if weight1 + weight == desired else idx + 1
                            explore(new_available, start_idx, mask1 | 1 << idx, weight1 + weight, mask2, weight2)

                try_mask >>= 1
                idx += 1

        weights = list(sorted(map(int, input_text), reverse=True))
        desired = sum(weights) // 3
        full_mask = (1 << len(weights)) - 1
        fewest_packages = sys.maxsize
        best_quantum = sys.maxsize
        solved = set()

        explore(full_mask, 0, 0, 0, 0, 0)

        return best_quantum
