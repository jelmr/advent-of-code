import unittest

from config import Config
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_example1(self):
        output = Solver(Config(
            hard_difficulty=False,
            base_player_hp=10,
            base_player_mana=250,
            base_boss_dmg=8,
            base_boss_hp=13,
        )).solve()
        self.assertEqual(output, 226)

    def test_example2(self):
        output = Solver(Config(
            hard_difficulty=False,
            base_player_hp=10,
            base_player_mana=250,
            base_boss_dmg=8,
            base_boss_hp=14,
        )).solve()
        self.assertEqual(output, 641)

    def test_part1(self):
        output = Solver(Config(
            hard_difficulty=False,
            base_player_hp=50,
            base_player_mana=500,
            base_boss_dmg=9,
            base_boss_hp=51,
        )).solve()
        self.assertEqual(output, 900)

    def test_part2(self):
        output = Solver(Config(
            hard_difficulty=True,
            base_player_hp=50,
            base_player_mana=500,
            base_boss_dmg=9,
            base_boss_hp=51,
        )).solve()
        self.assertEqual(output, 1216)


if __name__ == "__main__":
    unittest.main()
