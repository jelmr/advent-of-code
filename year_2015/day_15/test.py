import unittest

from year_2015.day_15.part1 import Part1
from year_2015.day_15.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(62842880, solver.solve([
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
        ]))

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(57600000, solver.solve([
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
        ]))


if __name__ == "__main__":
    unittest.main()
