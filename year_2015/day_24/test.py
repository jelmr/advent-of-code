import unittest

from year_2015.day_24.part1 import Part1
from year_2015.day_24.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(solver.solve(['1', '2', '3', '4', '5', '7', '8', '9', '10', '11']), 99)

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(solver.solve(['1', '2', '3', '4', '5', '7', '8', '9', '10', '11']), 44)


if __name__ == "__main__":
    unittest.main()
