from typing import List, Dict

from solution import Solution
from year_2015.day_16.parser import Parser


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        aunts = Parser().get_aunts(input_text)

        tape = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1,
        }

        def matches(aunt: Dict) -> bool:
            for k, v in tape.items():
                aunt_value = aunt.get(k, None)

                if k in ['cats', 'trees']:
                    if aunt_value is not None and aunt_value <= v:
                        return False
                elif k in ['pomeranians', 'goldfish']:
                    if aunt_value is not None and aunt_value >= v:
                        return False
                else:
                    if aunt_value is not None and aunt_value != v:
                        return False
            return True

        for idx, aunt in enumerate(aunts):
            if matches(aunt):
                return idx + 1
