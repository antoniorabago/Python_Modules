#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creature(factory: HealingCreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_creature(factory: TransformCreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    test_healing_creature(HealingCreatureFactory())

    print("\nTesting Creature with transform capability")
    test_transform_creature(TransformCreatureFactory())


if __name__ == "__main__":
    main()
