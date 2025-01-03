from abc import ABC, abstractmethod

from ..state import State


class Spell(ABC):
    @abstractmethod
    def cast(self, state: State):
        pass

    @abstractmethod
    def can_cast(self, state: State) -> bool:
        pass

    def tick(self, state: State):
        pass

    def __str__(self) -> str:
        return str(type(self)).split('_')[-1]

    def __repr__(self) -> str:
        return str(self)
