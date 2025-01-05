from typing import List


class Solver():
    def solve(self, password: str) -> str | int:
        password = list(password)
        Solver.increment(password)

        while not Solver.has_straight(password) or not Solver.has_two_pairs(password) or Solver.has_bad(password):
            if not Solver.remove_bad(password):
                Solver.increment(password)

        return ''.join(password)

    @staticmethod
    def increment(password: List[str]):
        for idx, c in reversed(list(enumerate(password))):
            if c == 'z':
                password[idx] = 'a'
            else:
                password[idx] = chr(ord(c) + 1)
                return

    @staticmethod
    def has_straight(password: List[str]) -> bool:
        for a, b, c in zip(password, password[1:], password[2:]):
            if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
                return True
        return False

    @staticmethod
    def has_bad(password: List[str]) -> bool:
        return any(c in 'iol' for c in password)

    @staticmethod
    def has_two_pairs(password: List[str]) -> bool:
        pairs = 0
        i = 0
        while i < len(password):
            if i > 0:
                current = password[i]
                prev = password[i - 1]
                if current == prev:
                    i += 1
                    pairs += 1
            i += 1
        return pairs >= 2

    @staticmethod
    def remove_bad(password: List[str]):
        removed = False
        for idx, c in reversed(list(enumerate(password))):
            if c in 'iol':
                password[idx] = chr(ord(c) + 1)
                password[idx + 1:] = ['a'] * len(password[idx + 1:])
                removed = True
        return removed
