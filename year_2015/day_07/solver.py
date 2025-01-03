import re
from collections import deque
from typing import List, Dict


class Solver():

    def __init__(self, variables: Dict[str, int]):
        self.variables = variables

    def solve(self, input_text: List[str]) -> int:

        def resolve(expression):
            # int
            if re.match(r'^\d+$', expression):
                return int(expression)
            # var
            if re.match(r'^[a-z]+$', expression):
                return self.variables[expression]
            # AND
            if re.match(r'^\w+ AND \w+$', expression):
                a, b = expression.split(' AND ')
                return resolve(a) & resolve(b)
            # OR
            if re.match(r'^\w+ OR \w+$', expression):
                a, b = expression.split(' OR ')
                return resolve(a) | resolve(b)
            # LSHIFT
            if re.match(r'^\w+ LSHIFT \d+$', expression):
                a, b = expression.split(' LSHIFT ')
                return resolve(a) << int(b)
            # RSHIFT
            if re.match(r'^\w+ RSHIFT \d+$', expression):
                a, b = expression.split(' RSHIFT ')
                return resolve(a) >> int(b)
            # NOT
            if re.match(r'^NOT \w+$', expression):
                a, b = expression.split('NOT ')
                return ~resolve(b)

            raise Exception('Cant resolve yet')

        queue = deque(input_text)

        while queue:
            line = queue.popleft()
            expression, variable = line.strip().split(' -> ')
            try:
                if variable not in self.variables:
                    self.variables[variable] = resolve(expression.strip()) & 0xFFFF
            except:
                queue.append(line)

        return self.variables['a']

