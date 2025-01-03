from typing import List

from solution import Solution


class Part1(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        x, y = 0, 0
        visited = {(x, y)}

        for direction in input_text[0]:
            match direction:
                case '>':
                    x += 1
                case '<':
                    x -= 1
                case '^':
                    y += 1
                case 'v':
                    y -= 1
            visited.add((x, y))
        return len(visited)



