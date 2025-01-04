from typing import List

from solution import Solution


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        def count(word: str) -> int:
            count = 0

            for c in word:
                if c in '\\"':
                    count += 1
                elif c == "'":
                    count += 2
                count += 1

            return count - len(word) + 2  # + 2 for the "

        return sum(map(count, input_text))
