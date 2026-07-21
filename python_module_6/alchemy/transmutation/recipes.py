from alchemy.elements import create_air
from ..potions import strength_potion
import elements


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew {create_air()!r} "
            f"and {strength_potion()!r} mixed with {elements.create_fire()!r}")
