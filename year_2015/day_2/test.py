import unittest

from year_2015.day_2.part1 import Part1
from year_2015.day_2.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(solver.solve(['2x3x4']), 58)
        self.assertEqual(solver.solve(['1x1x10']), 43)
        self.assertEqual(solver.solve(['2x3x4','1x1x10']), 101)

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(solver.solve(['2x3x4']), 34)
        self.assertEqual(solver.solve(['1x1x10']), 14)
        self.assertEqual(solver.solve(['2x3x4', '1x1x10']), 48)


if __name__ == "__main__":
    unittest.main()
