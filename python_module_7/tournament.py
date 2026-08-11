from ex0.creature import Creature
from ex0.creatureFactory import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex2.battleStrat import BattleStrategy
from ex1 import (HealingCreatureFactory, TransformCreatureFactory)
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def battle(opponent: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponent)} opponents involved")
    creatures: list[Creature] = [adv[0].create_base() for adv in opponent]
    strategy: list[BattleStrategy] = [strat[1] for strat in opponent]

    for i in range(len(opponent) - 1):
        for j in range(i + 1, len(opponent)):
            print()
            print("* Battle *")
            print(creatures[i].describe())
            print(" vs.")
            print(creatures[j].describe())
            print(" now fight!")
            try:
                strategy[i].act(creatures[i])
                strategy[j].act(creatures[j])
            except Exception as error:
                print(f"Battle error, aborting tournament: {error}")


if __name__ == "__main__":
    factory_flame: FlameFactory = FlameFactory()
    factory_water: AquaFactory = AquaFactory()

    factory_heal: HealingCreatureFactory = HealingCreatureFactory()
    factory_transform: TransformCreatureFactory = TransformCreatureFactory()

    normal_strat: NormalStrategy = NormalStrategy()
    defensive_strat: DefensiveStrategy = DefensiveStrategy()
    aggresive_strat: AggressiveStrategy = AggressiveStrategy()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(factory_flame, normal_strat), (factory_heal, defensive_strat)])
    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(factory_flame, aggresive_strat), (factory_heal, defensive_strat)])
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(factory_water, normal_strat), (factory_heal,
           defensive_strat), (factory_transform, aggresive_strat)])
