import re
from typing import List, Tuple


class Parser():

    def get_reindeers(self, input_text: List[str]) -> List[Tuple[int, int, int]]:
        """
        Example input:
            Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
            Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
        """
        reindeers = []

        for line in input_text:
            m = re.match(r'\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
            speed, fly_duration, rest_duration = map(int, m.groups())
            reindeers.append((speed, fly_duration, rest_duration))

        return reindeers
