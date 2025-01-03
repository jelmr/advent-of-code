import unittest

from year_2015.day_06.part1 import Part1
from year_2015.day_06.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_part1_1(self):
        solver = Part1()
        self.assertEqual(solver.solve([
            'toggle 0,0 through 99,99',
            'toggle 50,50 through 149,149',
        ]), 6 * 50 * 50)

    def test_part1_2(self):
        solver = Part1()
        self.assertEqual(solver.solve([
            'toggle 0,0 through 99,99',
            'toggle 50,50 through 149,149',
            'turn off 0,0 through 149,149',
            'turn on 0,0 through 99,99',
            'toggle 50,50 through 149,149',
        ]), 6 * 50 * 50)

    def test_part1_3(self):
        solver = Part1()
        self.assertEqual(solver.solve([
            'turn on 0,0 through 99,99',
            'toggle 50,50 through 149,149',
            'toggle 110,25 through 139,74',
        ]), 6 * 50 * 50)

    def test_part1_4(self):
        solver = Part1()
        self.assertEqual(solver.solve([
            'turn on 0,0 through 99,99',
            'toggle 50,50 through 149,149',
            'turn on 110,25 through 139,74',
        ]), 6 * 50 * 50 + 25*30)

    def test_part1_5(self):
        solver = Part1()
        self.assertEqual(solver.solve([
            'turn on 0,0 through 99,99',
            'toggle 50,50 through 149,149',
            'turn off 110,25 through 139,74',
        ]), 6 * 50 * 50 - 25*30)

    def test_part2_1(self):
        solver = Part2()
        self.assertEqual(solver.solve([
            'turn on 0,0 through 0,0',
        ]), 1)

    def test_part2_2(self):
        solver = Part2()
        self.assertEqual(solver.solve([
            'toggle 0,0 through 999,999',
        ]), 2000000)


if __name__ == "__main__":
    unittest.main()
