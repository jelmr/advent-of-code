from Spells.spell import Spell
from state import State


class Recharge(Spell):
    MANA_COST = 229
    POWER = 101
    TURNS = 5

    def cast(self, state: State):
        state.spend_mana(self.MANA_COST)
        state.recharge_turns = self.TURNS

    def can_cast(self, state: State) -> bool:
        return state.mana >= self.MANA_COST and state.recharge_turns == 0

    def tick(self, state: State):
        if state.recharge_turns > 0:
            state.mana += self.POWER
            state.recharge_turns -= 1
