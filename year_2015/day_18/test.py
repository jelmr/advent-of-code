import unittest

from year_2015.day_18.part1 import Part1
from year_2015.day_18.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(4, solver.run_generations([
            '.#.#.#',
            '...##.',
            '#....#',
            '..#...',
            '#.#..#',
            '####..',
        ], 4))

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(17, solver.run_generations([
            '.#.#.#',
            '...##.',
            '#....#',
            '..#...',
            '#.#..#',
            '####..',
        ], 5))


if __name__ == "__main__":
    unittest.main()
