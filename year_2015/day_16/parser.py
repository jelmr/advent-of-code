import re
from typing import List, Dict



class Parser():

    def get_aunts(self, input_text: List[str]) -> List[Dict]:
        """
        Example input:
            Sue 1: children: 1, cars: 8, vizslas: 7
            Sue 2: akitas: 10, perfumes: 10, children: 5
            Sue 3: cars: 5, pomeranians: 4, vizslas: 1
            Sue 4: goldfish: 5, children: 8, perfumes: 3
        """
        aunts = []

        for line in input_text:
            sue_match = re.match(r'^Sue (\d+): ', line)
            sue_nr = sue_match.groups()[0]

            aunt = {}

            properties = re.findall(r'(\w+): (\d+)', line)
            for property, value in properties:
                aunt[property] = int(value)

            aunts.append(aunt)

        return aunts
