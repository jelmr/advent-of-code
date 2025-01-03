from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Config:
    hard_difficulty: bool
    base_player_hp: int
    base_player_mana: int
    base_boss_hp: int
    base_boss_dmg: int
