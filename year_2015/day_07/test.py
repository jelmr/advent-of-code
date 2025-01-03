import unittest

from year_2015.day_07.part1 import Part1


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        base_program = [
            '123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i',
        ]
        self.assertEqual(72, solver.solve(base_program + ['d -> a'])),
        self.assertEqual(507, solver.solve(base_program + ['e -> a'])),
        self.assertEqual(492, solver.solve(base_program + ['f -> a'])),
        self.assertEqual(114, solver.solve(base_program + ['g -> a'])),
        self.assertEqual(65412, solver.solve(base_program + ['h -> a'])),
        self.assertEqual(65079, solver.solve(base_program + ['i -> a'])),
        self.assertEqual(123, solver.solve(base_program + ['x -> a'])),
        self.assertEqual(456, solver.solve(base_program + ['y -> a'])),


if __name__ == "__main__":
    unittest.main()
