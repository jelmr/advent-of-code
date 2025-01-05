import unittest

from year_2015.day_10.part1 import Part1
from year_2015.day_10.part2 import Part2
from year_2015.day_10.solver import Solver


class TestSolver(unittest.TestCase):
    def test_steps(self):
        solver = Solver()
        self.assertEqual(2, solver.steps('1',1))
        self.assertEqual(2, solver.steps('11',1))
        self.assertEqual(4, solver.steps('21',1))
        self.assertEqual(6, solver.steps('1211',1))
        self.assertEqual(6, solver.steps('111221',1))
        self.assertEqual(6, solver.steps('1',5))


if __name__ == "__main__":
    unittest.main()
