from collections import defaultdict
from typing import Tuple, List


class Solver:
    def calculate_distance(self, reindeer: Tuple[int, int, int], total_duration) -> int:
        speed, fly_duration, rest_duration = reindeer

        cycle_duration = fly_duration + rest_duration
        full_cycles = total_duration // cycle_duration
        full_cycle_distance = full_cycles * speed * fly_duration

        remaining_duration = total_duration % cycle_duration
        remaining_fly_duration = min(fly_duration, remaining_duration)
        remaining_distance = remaining_fly_duration * speed

        return full_cycle_distance + remaining_distance

    def calculate_score(self, reindeers: List[Tuple[int, int, int]], total_duration) -> int:
        # This is not a very efficient solution, but the input is tiny, so I prioritised simple code of execution time
        scores = defaultdict(int)

        for second in range(1, total_duration):
            lead = max(self.calculate_distance(reindeer, second) for reindeer in reindeers)
            for reindeer in reindeers:
                distance = self.calculate_distance(reindeer, second)
                if distance == lead:
                    scores[reindeer] += 1

        return max(scores.values())



