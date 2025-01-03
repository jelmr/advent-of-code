from itertools import pairwise
from typing import List

from more_itertools import quantify

from solution import Solution


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        def is_nice(word: str) -> bool:
            return self.has_double_pair(word) and self.has_repeated_letter(word)

        return quantify(input_text, pred=is_nice)

    @staticmethod
    def has_double_pair(word: str) -> bool:
        pair_first_seen = {}
        for idx, (a, b) in enumerate(pairwise(word)):
            pair = a + b
            if pair not in pair_first_seen:
                pair_first_seen[pair] = idx
            elif idx - pair_first_seen[pair] >= 2:
                return True
        return False

    @staticmethod
    def has_repeated_letter(word: str) -> bool:
        for a, b, c in zip(word, word[1:], word[2:]):
            if a == c:
                return True
        return False
