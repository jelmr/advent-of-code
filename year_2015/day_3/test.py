import unittest

from year_2015.day_3.part1 import Part1
from year_2015.day_3.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(solver.solve(['>']), 2)
        self.assertEqual(solver.solve(['^>v<']), 4)
        self.assertEqual(solver.solve(['^v^v^v^v^v']), 2)

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(solver.solve(['^v']), 3)
        self.assertEqual(solver.solve(['^>v<']), 3)
        self.assertEqual(solver.solve(['^v^v^v^v^v']), 11)


if __name__ == "__main__":
    unittest.main()
