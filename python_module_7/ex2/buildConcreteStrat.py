from .battleStrat import BattleStrategy
from ex0.creature import Creature
from ex1.healCap import HealCapability
from ex1.transformCap import TransformCapability


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if not isinstance(creature, Creature):
            return False
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception("Error in creature strategy")
        else:
            print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature {creature.name!r} "
                f"for this aggressive strategy")
        elif isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature {creature.name!r} "
                f"for this defensive strategy")
        elif isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())
