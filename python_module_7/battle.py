from ex0 import FlameFactory, AquaFactory
from ex0.creature import Creature
from ex0.creatureFactory import CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    try:
        base_creature: Creature = factory.create_base()
        print(base_creature.describe())
        print(base_creature.attack())
        evolved_creature = factory.create_evolved()
        print(evolved_creature.describe())
        print(evolved_creature.attack())
    except Exception:
        print("Error creature creation")


def testing_battle(flame_factory: CreatureFactory,
                   aqua_factory: CreatureFactory) -> None:
    print("Testing Battle")
    try:
        flame_creature: Creature = flame_factory.create_base()
        aqua_creature: Creature = aqua_factory.create_base()
        print(flame_creature.describe())
        print(" vs.")
        print(aqua_creature.describe())
        print(" fight!")
        print(flame_creature.attack())
        print(aqua_creature.attack())
    except Exception:
        print("Error creature battle...")


if __name__ == "__main__":
    flame_type: FlameFactory = FlameFactory()
    aqua_type: AquaFactory = AquaFactory()
    testing_factory(flame_type)
    print()
    testing_factory(aqua_type)
    print()
    testing_battle(flame_type, aqua_type)
