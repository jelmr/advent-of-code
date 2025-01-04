from typing import List

from solution import Solution


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        def count(word: str) -> int:
            word = word.strip()[1:-1]  # remove "
            memory = 0
            code = 0
            while code < len(word):
                if word[code] == '\\' and code < len(word) - 1:
                    if word[code + 1] in '\\"':
                        code += 1
                    elif word[code + 1] == 'x':
                        code += 3
                code += 1
                memory += 1
            return code - memory + 2  # add 2 because we stripped a " from start and end

        return sum(map(count, input_text))
