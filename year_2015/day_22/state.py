from __future__ import annotations

from dataclasses import dataclass


@dataclass
class State:
    player_hp: int
    boss_hp: int
    mana: int
    mana_spent: int = 0
    armor: int = 0

    poison_turns: int = 0
    shield_turns: int = 0
    recharge_turns: int = 0

    def __lt__(self, other: State):
        return self.mana_spent < other.mana_spent

    def spend_mana(self, mana: int):
        self.mana -= mana
        self.mana_spent += mana
