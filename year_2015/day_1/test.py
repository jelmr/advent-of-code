import unittest

from year_2015.day_1.part1 import Part1
from year_2015.day_1.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(solver.solve(['(())']), 0)
        self.assertEqual(solver.solve(['()()']), 0)
        self.assertEqual(solver.solve(['))(((((']), 3)
        self.assertEqual(solver.solve(['(((']), 3)
        self.assertEqual(solver.solve(['(()(()(']), 3)
        self.assertEqual(solver.solve(['())']), -1)
        self.assertEqual(solver.solve(['))(']), -1)
        self.assertEqual(solver.solve([')))']), -3)
        self.assertEqual(solver.solve([')())())']), -3)

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(solver.solve([')']), 1)
        self.assertEqual(solver.solve(['()())']), 5)


if __name__ == "__main__":
    unittest.main()
