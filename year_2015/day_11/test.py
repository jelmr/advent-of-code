import unittest

from year_2015.day_11.part1 import Part1
from year_2015.day_11.solver import Solver


class TestSolver(unittest.TestCase):
    def test_examples_part1(self):
        solver = Part1()
        self.assertEqual('abcdffaa', solver.solve(['abcdefgh']))
        self.assertEqual('ghjaabcc', solver.solve(['ghijklmn']))
        self.assertEqual('hepxxyzz', solver.solve(['hepxcrrq']))

    def test_remove_bad(self):
        solver = Solver()

        def test(password: str, expected: str, changed: bool):
            p = list(password)
            res = solver.remove_bad(p)
            self.assertEqual(changed, res)
            self.assertEqual(expected, ''.join(p))

        test('abcdefgh', 'abcdefgh', False)
        test('abcdefgi', 'abcdefgj', True)
        test('abciefga', 'abcjaaaa', True)
        test('lbcdefgh', 'maaaaaaa', True)
        test('abodlfih', 'abpaaaaa', True)

    def test_increment(self):
        solver = Solver()

        def test(password: str, expected: str):
            p = list(password)
            solver.increment(p)
            self.assertEqual(expected, ''.join(p))

        test('abcdefgh', 'abcdefgi')
        test('abcdefgi', 'abcdefgj')
        test('hepxxyzz', 'hepxxzaa')

    def test_has_straight(self):
        self.assertFalse(Solver.has_straight(list('aaa')))
        self.assertFalse(Solver.has_straight(list('qpzmxm')))
        self.assertFalse(Solver.has_straight(list('0')))
        self.assertFalse(Solver.has_straight(list('ooxpp')))
        self.assertFalse(Solver.has_straight(list('abxd')))
        self.assertFalse(Solver.has_straight(list('abd')))
        self.assertTrue(Solver.has_straight(list('abc')))
        self.assertTrue(Solver.has_straight(list('abxacabc')))
        self.assertTrue(Solver.has_straight(list('abmno')))
        self.assertTrue(Solver.has_straight(list('qrs')))
        self.assertTrue(Solver.has_straight(list('abqrsab')))

    def test_has_bad(self):
        self.assertFalse(Solver.has_bad(list('aaa')))
        self.assertFalse(Solver.has_bad(list('qpzmxm')))
        self.assertFalse(Solver.has_bad(list('0')))
        self.assertTrue(Solver.has_bad(list('ooxpp')))
        self.assertTrue(Solver.has_bad(list('iaaa')))
        self.assertTrue(Solver.has_bad(list('l')))

    def test_has_two_pairs(self):
        self.assertFalse(Solver.has_two_pairs(list('aaa')))
        self.assertFalse(Solver.has_two_pairs(list('a')))
        self.assertFalse(Solver.has_two_pairs(list('x')))
        self.assertFalse(Solver.has_two_pairs(list('ab')))
        self.assertFalse(Solver.has_two_pairs(list('aabc')))
        self.assertFalse(Solver.has_two_pairs(list('oqpoqp')))
        self.assertTrue(Solver.has_two_pairs(list('ooxpp')))
        self.assertTrue(Solver.has_two_pairs(list('aaaa')))
        self.assertTrue(Solver.has_two_pairs(list('aabcdebb')))


if __name__ == "__main__":
    unittest.main()
