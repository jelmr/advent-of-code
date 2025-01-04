from collections import deque
from itertools import combinations
from typing import List, Tuple


class HeldKarp():
    """
    Solves the Traveling Salesmen Problem, and returns the length of the shortest path
    that travels to all nodes in `distances`
    """

    def __init__(self, fixed_start=True, back_to_start=True, longest_distance=False):
        """
        :param fixed_start: If true, it will only evaluate routes starting at node 0, otherwise it tries all nodes as starting position.
        :param back_to_start: If true, the path must end at the starting location, otherwise it ends at a random node.
        :param longest_distance: If true, finds the longest path instead of the shortest path
        """
        self.fixed_start = fixed_start
        self.back_to_start = back_to_start
        self.longest_path = longest_distance

    def best_total_distance(self, dist: List[List[int]]) -> int:
        return self.held_karp(dist)[0]

    def get_best(self):
        return max if self.longest_path else min

    def held_karp(self, dist: List[List[int]]) -> Tuple[int, List[int]]:
        def rotate(dist: List[List[int]], n: int) -> List[List[int]]:
            """
            Rotate the dist matrix by n positions, so that a different city is in first position
            """
            before = [row[n:] + row[:n] for row in dist[n:]]
            after = [row[n:] + row[:n] for row in dist[:n]]
            return before + after

        if self.fixed_start:
            return self._held_karp(dist)
        else:
            # Try the algorithm with every node as starting position
            (best_cost, best_path), rotations = self.get_best()(
                (self._held_karp(rotate(dist, n)), n)
                for n in range(len(dist))
            )
            return best_cost, [(c + rotations) % len(dist) for c in best_path]  # correct the best_path indexes

    def _held_karp(self, dist: List[List[int]]) -> Tuple[int, List[int]]:
        """
        Default Held Karp algorthim

        :param dist: A 2D distance matrix, where distances[i][j] is the cost of traveling from i to j
        :return: Length of the shortest path visiting all nodes
        """

        N = len(dist)

        # dp[mask][i] stores a tuple of:
        #   - lowest cost of visiting all cities described by `mask`, while ending at i
        #   - the city visited before i
        dp = {}

        # set initial distances
        for c in range(1, N):
            dp[(1 << c, c)] = (dist[0][c], 0)

        for subset_size in range(2, N):
            for subset in combinations(range(1, N), subset_size):
                mask = 0
                for bit in subset:
                    mask |= 1 << bit

                for last in subset:
                    mask_without_last = mask & ~(1 << last)
                    dp[(mask, last)] = self.get_best()(
                        (dp[(mask_without_last, prev)][0] + dist[prev][last], prev)
                        for prev in subset
                        if prev != 0 and prev != last
                    )
        # All cities, except the first
        final_mask = (2 ** N - 1) - 1

        best_total_distance, final_node = self.get_best()(
            (dp[(final_mask, last)][0] + (dist[last][0] if self.back_to_start else 0), last)
            # add the cost of going back to the start if necessary
            for last in range(1, N)
        )

        # Reconstruct the taken path
        path = deque()
        current = final_node
        for i in range(N - 1):
            path.appendleft(current)
            mask_without_parent = final_mask & ~(1 << current)
            _, current = dp[(final_mask, current)]
            final_mask = mask_without_parent
        path.appendleft(0)

        return best_total_distance, list(path)
