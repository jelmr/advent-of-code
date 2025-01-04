import re
from collections import defaultdict
from typing import List


class Parser():

    def get_distance_matrix(self, input_text: List[str]) -> List[List[int]]:
        """
        Example input:
            London to Dublin = 464
            London to Belfast = 518
            Dublin to Belfast = 141
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
            m = re.match(r'(\w+) to (\w+) = (\d+)', line)
            src, dst, cost = m.groups()
            src_id, dst_id = get_id(src), get_id(dst)
            dist[src_id][dst_id] = int(cost)
            dist[dst_id][src_id] = int(cost)
            dist[src_id][src_id] = 0
            dist[dst_id][dst_id] = 0

        return [ # convert to 2d list
            [
                v for k, v in sorted(r.items())
            ] for k, r in sorted(dist.items())
        ]
