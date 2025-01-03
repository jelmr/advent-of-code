from solution import Solution
from .config import Config
from .solver import Solver


class Part1(Solution):
    def solve(self, input_text: str):
        return Solver(Config(
            hard_difficulty=False,
            base_player_hp=50,
            base_player_mana=500,
            base_boss_dmg=9,
            base_boss_hp=51,
        )).solve()
