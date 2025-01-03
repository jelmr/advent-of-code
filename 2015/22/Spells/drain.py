from Spells.spell import Spell
from state import State


class Drain(Spell):
    MANA_COST = 73
    POWER = 2

    def cast(self, state: State):
        state.spend_mana(self.MANA_COST)
        state.player_hp += self.POWER
        state.boss_hp -= self.POWER

    def can_cast(self, state: State) -> bool:
        return state.mana >= self.MANA_COST
