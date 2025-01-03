from Spells.spell import Spell
from state import State


class MagicMissile(Spell):
    MANA_COST = 53
    POWER = 4

    def cast(self, state: State):
        state.spend_mana(self.MANA_COST)
        state.boss_hp -= self.POWER

    def can_cast(self, state: State) -> bool:
        return state.mana >= self.MANA_COST
