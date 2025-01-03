import unittest

from year_2015.day_04.part1 import Part1
from year_2015.day_04.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(solver.solve(['abcdef']), 609043)
        self.assertEqual(solver.solve(['pqrstuv']), 1048970)

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(solver.solve(['ckczppom']),  3938038)


if __name__ == "__main__":
    unittest.main()
