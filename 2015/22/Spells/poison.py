from Spells.spell import Spell
from state import State


class Poison(Spell):
    MANA_COST = 173
    POWER = 3
    TURNS = 6

    def cast(self, state: State):
        state.spend_mana(self.MANA_COST)
        state.poison_turns = self.TURNS

    def can_cast(self, state: State) -> bool:
        return state.mana >= self.MANA_COST and state.poison_turns == 0

    def tick(self, state: State):
        if state.poison_turns > 0:
            state.boss_hp -= self.POWER
            state.poison_turns -= 1
