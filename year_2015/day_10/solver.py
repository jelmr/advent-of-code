class Solver:
    def steps(self, word: str, steps: int) -> int:
        current_word = word

        for i in range(steps):
            current_word = self.do_step(current_word)

        return len(current_word)

    def do_step(self, word: str) -> str:
        last = None
        count = 0
        result = ''

        for c in word:
            if c == last:
                count += 1
            else:
                if last is not None:
                    result += str(count) + str(last)
                last = c
                count = 1
        if last is not None:
            result += str(count) + str(last)

        return result
