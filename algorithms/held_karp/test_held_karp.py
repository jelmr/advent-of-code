import unittest

from algorithms.held_karp.held_karp import HeldKarp


class TestHeldKarp(unittest.TestCase):

    def test1(self):
        result = HeldKarp(fixed_start=True, back_to_start=True).best_total_distance([
            [0, 464, 518],
            [464, 0, 141],
            [518, 141, 0]
        ])
        self.assertEqual(464 + 518 + 141, result)


if __name__ == '__main__':
    unittest.main()
