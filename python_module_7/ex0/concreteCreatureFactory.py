from .creatureFactory import CreatureFactory
from .concreteCreature import Aquabub, Flameling, Pyrodon, Torragon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling("Flameling", "fire")

    def create_evolved(self) -> Pyrodon:
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Torragon:
        return Torragon("Torragon", "Water")
