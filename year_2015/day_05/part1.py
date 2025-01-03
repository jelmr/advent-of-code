from itertools import pairwise
from typing import List
from more_itertools import quantify

from solution import Solution


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        def is_nice(word: str) -> bool:
            contains_bad = any(bad in word for bad in ['ab', 'cd', 'pq', 'xy'])
            contains_enough_vowels = quantify(word, pred=lambda c: c in 'aeiou') >= 3
            contains_double = any(a == b for a, b in pairwise(word))
            return not contains_bad and contains_double and contains_enough_vowels

        return quantify(input_text, pred=is_nice)

