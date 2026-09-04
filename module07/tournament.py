#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, AggressiveStrategy, DefensiveStrategy, \
                NormalStrategy, InvalidStrategyError


def battle(oponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    total_creatures = len(oponents)
    print(f"{total_creatures} opponents involved")
    creatures = []
    for factory, strategy in oponents:
        creature = factory.create_base()
        creatures.append((creature, strategy))
    for i in range(total_creatures):
        creature1, strategy1 = creatures[i]
        for j in range(i+1, total_creatures):
            creature2, strategy2 = creatures[j]
            print("\n* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    agresive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    normal_strategy = NormalStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    oponents = [(flame_factory, normal_strategy),
                (heal_factory, defensive_strategy)]
    battle(oponents)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    oponents = [(flame_factory, agresive_strategy),
                (heal_factory, defensive_strategy)]
    battle(oponents)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    oponents = [(aqua_factory, normal_strategy),
                (heal_factory, defensive_strategy),
                (transform_factory, agresive_strategy)]
    battle(oponents)


if __name__ == "__main__":
    main()
