from typing import List

from solution import Solution


class Part2(Solution):
    def solve(self, input_text: List[str]) -> str | int:
        visited = {(0, 0)}

        for agent_idx in 0, 1:
            x, y = 0, 0
            for direction in input_text[0][agent_idx::2]:
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
