import hashlib
from typing import List


class HashFinder():

    def __init__(self, input_text: List[str]):
        self.input_text = input_text

    def solve(self, prefix: str) -> str | int:
        n = 1
        while True:
            key = self.input_text[0] + str(n)
            md5_hash = hashlib.md5(key.encode()).hexdigest()
            if md5_hash.startswith(prefix):
                return n
            n += 1
