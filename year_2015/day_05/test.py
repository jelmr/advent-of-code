import unittest

from year_2015.day_05.part1 import Part1
from year_2015.day_05.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(solver.solve(['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']), 2)

    def test_double_words(self):
        self.assertTrue(Part2.has_double_pair('xyxy'))
        self.assertTrue(Part2.has_double_pair('aabcdefgaa'))
        self.assertFalse(Part2.has_double_pair('aaa'))

    def test_repeated_letter(self):
        self.assertTrue(Part2.has_repeated_letter('xyx'))
        self.assertTrue(Part2.has_repeated_letter('abcdefeghi'))
        self.assertTrue(Part2.has_repeated_letter('aaa'))
        self.assertFalse(Part2.has_repeated_letter('abc'))
        self.assertFalse(Part2.has_repeated_letter('abba'))

    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(solver.solve(['qjhvhtzxzqqjkmpb']), 1)
        self.assertEqual(solver.solve(['xxyxx']), 1)
        self.assertEqual(solver.solve(['uurcxstgmygtbstg']), 0)
        self.assertEqual(solver.solve(['ieodomkazucvgmuy']), 0)
        self.assertEqual(solver.solve(['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']), 2)


if __name__ == "__main__":
    unittest.main()
