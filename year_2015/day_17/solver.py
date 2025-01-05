import sys
from typing import List, Tuple


class Solver:

    def combinations(self, containers: List[int], target: int, allowed_containers: None|int = None) -> Tuple[int, int]:
        count = 0
        least_containers = sys.maxsize

        if allowed_containers is None:
            allowed_containers = len(containers)

        def go(idx: int, remaining: int, num_containers: int):
            if remaining == 0:
                nonlocal count, least_containers
                count += 1
                least_containers = min(least_containers, num_containers)
                return

            if remaining < 0 or idx == len(containers) or num_containers == allowed_containers:
                return

            container = containers[idx]
            go(idx + 1, remaining - container, num_containers + 1)
            go(idx + 1, remaining, num_containers)

        go(0, target, 0)
        return count, least_containers

