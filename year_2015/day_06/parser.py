import re
from typing import List, Tuple, Iterator, Literal

Action = Literal["turn on", "turn off", "toggle"]
Instruction = Tuple[Action, Tuple[int, int], Tuple[int, int]]


class Parser:

    def __init__(self, input_text: List[str]):
        self.input_text = input_text

    def get_instructions(self) -> Iterator[Instruction]:
        for line in self.input_text:
            yield self.parse_line(line)

    def parse_line(self, line) -> Instruction:
        m = re.match(r'^(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)$', line)

        if not m:
            raise ValueError(f'Cannot parse line: {line}')

        action = m.group(1)
        x1, y1 = int(m.group(2)), int(m.group(3))
        x2, y2 = int(m.group(4)), int(m.group(5))
        return action, (x1, y1), (x2, y2)
