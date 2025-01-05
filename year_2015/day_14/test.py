import unittest

from year_2015.day_14.part2 import Part2
from year_2015.day_14.solver import Solver


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Solver()
        self.assertEqual(1120, solver.calculate_distance((14, 10, 127), 1000))
        self.assertEqual(1056, solver.calculate_distance((16, 11, 162), 1000))

    def test_examples_part2(self):
        solver = Solver()
        self.assertEqual(139, solver.calculate_score([(14, 10, 127), (16, 11, 162)], 140))
        self.assertEqual(689, solver.calculate_score([(14, 10, 127), (16, 11, 162)], 1000))


if __name__ == "__main__":
    unittest.main()
