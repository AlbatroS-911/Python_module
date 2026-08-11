from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_factory(heal_factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    try:
        heal_base_creature: Creature
        heal_evolved_creature: Creature
        heal_base_creature = heal_factory.create_base()
        heal_evolved_creature = heal_factory.create_evolved()
        print(" base:")
        print(heal_base_creature.describe())
        print(heal_base_creature.attack())
        print(heal_base_creature.heal())
        print(" evolved:")
        print(heal_evolved_creature.describe())
        print(heal_evolved_creature.attack())
        print(heal_evolved_creature.heal())
    except Exception:
        print("Error Healing Creature creation...")


def test_transform_factory(transform_factory:
                           TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    try:
        trans_base_creature: Creature
        trans_evolved_creature: Creature
        trans_base_creature = transform_factory.create_base()
        trans_evolved_creature = transform_factory.create_evolved()
        print(" base:")
        print(trans_base_creature.describe())
        print(trans_base_creature.attack())
        print(trans_base_creature.transform())
        print(trans_base_creature.attack())
        print(trans_base_creature.revert())
        print(" evolved:")
        print(trans_evolved_creature.describe())
        print(trans_evolved_creature.attack())
        print(trans_evolved_creature.transform())
        print(trans_evolved_creature.attack())
        print(trans_evolved_creature.revert())
    except Exception:
        print("Error Transformed Creature creation...")


if __name__ == "__main__":
    heal_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()
    test_heal_factory(heal_factory)
    print()
    test_transform_factory(transform_factory)
