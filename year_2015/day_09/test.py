import unittest

from year_2015.day_09.part1 import Part1
from year_2015.day_09.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(solver.solve([
            'London to Dublin = 464',
            'London to Belfast = 518',
            'Dublin to Belfast = 141',
        ]), 605)

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(solver.solve([
            'London to Dublin = 464',
            'London to Belfast = 518',
            'Dublin to Belfast = 141',
        ]), 982)


if __name__ == "__main__":
    unittest.main()
