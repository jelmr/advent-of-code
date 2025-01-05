import re
from collections import defaultdict
from typing import List


class Parser():

    def get_happiness_matrix(self, input_text: List[str]) -> List[List[int]]:
        """
        Example input:
            Bob would gain 83 happiness units by sitting next to Alice.
            Bob would lose 7 happiness units by sitting next to Carol.
            Bob would lose 63 happiness units by sitting next to David.
            Carol would lose 62 happiness units by sitting next to Alice.
            Carol would gain 60 happiness units by sitting next to Bob.
        """

        dist = defaultdict(dict)

        current_id = 0
        names = {}

        def get_id(name: str) -> int:
            nonlocal current_id
            if name not in names:
                names[name] = current_id
                current_id += 1
            return names[name]

        for line in input_text:
            m = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)
            person, effect, magnitude, neighbor  = m.groups()
            person_id, neighbor_id = get_id(person), get_id(neighbor)
            sign = -1 if effect == 'lose' else 1
            dist[person_id][neighbor_id] = sign * int(magnitude)
            dist[person_id][person_id] = 0

        return [ # convert to 2d list
            [
                v for k, v in sorted(r.items())
            ] for k, r in sorted(dist.items())
        ]
