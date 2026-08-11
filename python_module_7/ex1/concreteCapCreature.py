from .healCap import HealCapability
from .transformCap import TransformCapability
from ex0.creature import Creature


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.transformed: bool = False

    def attack(self) -> str:
        if not self.transformed:
            return (f"{self.name} attacks normally")
        return (f"{self.name} performs a boosted strike!")

    def transform(self) -> str:
        self.transformed = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.transformed: bool = False

    def attack(self) -> str:
        if not self.transformed:
            return (f"{self.name} attacks normally.")
        return (f"{self.name} unleashes a devastating morph strike!")

    def transform(self) -> str:
        self.transformed = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        return (f"{self.name} stabilizes its form.")
