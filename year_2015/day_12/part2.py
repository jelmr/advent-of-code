from typing import List

from solution import Solution
from year_2015.day_12.part1 import Part1


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        text = input_text[0]

        def find(idx, step):
            good = '{' if step == -1 else '}'
            bad = '}' if step == -1 else '{'

            count = 1

            while count != 0:
                if text[idx] == good:
                    count -= 1
                elif text[idx] == bad:
                    count += 1
                idx += step

            return idx

        while ':"red"' in text:
            idx = text.find(':"red"')
            start = find(idx, -1)
            end = find(idx, 1)
            text = text[:start + 1] + text[end:]

        return Part1().solve([text])
