import unittest

from year_2015.day_17.part1 import Part1
from year_2015.day_17.part2 import Part2
from year_2015.day_17.solver import Solver


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Solver()
        count, least_containers = solver.combinations([20, 15, 10, 5, 5], 25)
        self.assertEqual(4, count)
        self.assertEqual(2, least_containers)


    def test_examples_part2(self):
        solver = Solver()
        count, least_containers = solver.combinations([20, 15, 10, 5, 5], 25, allowed_containers=2)
        self.assertEqual(3, count)
        self.assertEqual(2, least_containers)


if __name__ == "__main__":
    unittest.main()
