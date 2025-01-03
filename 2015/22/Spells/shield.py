from Spells.spell import Spell
from state import State


class Shield(Spell):
    MANA_COST = 113
    POWER = 7
    TURNS = 6

    def cast(self, state: State):
        state.spend_mana(self.MANA_COST)
        state.armor += self.POWER
        state.shield_turns = self.TURNS

    def can_cast(self, state: State) -> bool:
        return state.mana >= self.MANA_COST and state.shield_turns == 0

    def tick(self, state: State):
        if state.shield_turns > 0:
            state.shield_turns -= 1
            if state.shield_turns == 0:
                state.armor -= self.POWER
