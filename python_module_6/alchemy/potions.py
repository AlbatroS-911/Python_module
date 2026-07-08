import elements
import alchemy


def healing_potion() -> str:
    earth: str = alchemy.elements.create_earth()
    air: str = alchemy.elements.create_air()
    return f"Healing potion brewed with {earth!r} and {air!r}"


def strength_potion() -> str:
    fire: str = elements.create_fire()
    water: str = elements.create_water()
    return f"Strength potion brewed with {fire!r} and {water!r}"
