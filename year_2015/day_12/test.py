import unittest

from year_2015.day_12.part1 import Part1
from year_2015.day_12.part2 import Part2


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual(6, solver.solve(['[1,2,3]']))
        self.assertEqual(6, solver.solve(['{"a":2,"b":4}']))
        self.assertEqual(3, solver.solve(['[[[3]]]']))
        self.assertEqual(3, solver.solve(['{"a":{"b":4},"c":-1}']))
        self.assertEqual(0, solver.solve(['{"a":[-1,1]}']))
        self.assertEqual(0, solver.solve(['[-1,{"a":1}]']))
        self.assertEqual(0, solver.solve(['[]']))
        self.assertEqual(0, solver.solve(['{}']))


    def test_examples_part2(self):
        solver = Part2()
        self.assertEqual(6, solver.solve(['[1,2,3]']))
        self.assertEqual(4, solver.solve(['[1,{"c":"red","b":2},3]']))
        self.assertEqual(0, solver.solve(['{"d":"red","e":[1,2,3,4],"f":5}']))
        self.assertEqual(6, solver.solve(['[1,"red",5]']))


if __name__ == "__main__":
    unittest.main()
