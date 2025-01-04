import unittest

from year_2015.day_08.part1 import Part1
from year_2015.day_08.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(2, solver.solve(['""']))
        self.assertEqual(2, solver.solve(['"abc"']))
        self.assertEqual(3, solver.solve(['"aaa\\"aaa"']))
        self.assertEqual(5, solver.solve(['"\\x27"']))
        self.assertEqual(12, solver.solve(['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']))
        self.assertEqual(9, solver.solve(['"\\xa8br\\x8bjr\\""']))

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(4, solver.solve(['""']))
        self.assertEqual(4, solver.solve(['"abc"']))
        self.assertEqual(6, solver.solve(['"aaa\\"aaa"']))
        self.assertEqual(5, solver.solve(['"\\x27"']))
        self.assertEqual(19, solver.solve(['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']))


if __name__ == "__main__":
    unittest.main()
