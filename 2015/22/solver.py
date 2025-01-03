import copy
import heapq
import math
from typing import Iterator, List

from Spells import MagicMissile, Drain, Shield, Poison, Recharge
from state import State


class Solver:

    def __init__(self, config):
        self.spells = [MagicMissile(), Drain(), Shield(), Poison(), Recharge()]
        self.config = config

    def get_initial_state(self) -> State:
        return State(
            player_hp=self.config.base_player_hp,
            boss_hp=self.config.base_boss_hp,
            mana=self.config.base_player_mana,
        )

    def tick(self, state: State):
        for spell in self.spells:
            spell.tick(state)

    def do_possible_player_turns(self, state: State) -> Iterator[State]:
        if self.config.hard_difficulty:
            state.player_hp -= 1

        if state.player_hp >= 0:
            self.tick(state)

            for spell in self.spells:
                if spell.can_cast(state):
                    new_state: State = copy.copy(state)
                    spell.cast(new_state)
                    yield new_state

    def do_boss_turn(self, state: State):
        self.tick(state)
        if state.boss_hp > 0:
            dmg = max(1, self.config.base_boss_dmg - state.armor)
            state.player_hp -= dmg

    def solve(self):
        best_victory = float('inf')
        queue: List[State] = [self.get_initial_state()]

        while queue and queue[0].mana_spent < best_victory:
            state: State = heapq.heappop(queue)

            for new_state in self.do_possible_player_turns(state):
                self.do_boss_turn(new_state)

                if new_state.player_hp > 0:
                    if new_state.boss_hp <= 0:
                        best_victory = min(best_victory, new_state.mana_spent)
                    else:
                        heapq.heappush(queue, new_state)

        return None if math.isinf(best_victory) else best_victory
