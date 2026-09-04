#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    healing_creature = HealingCreatureFactory()
    base_healing = healing_creature.create_base()
    print(base_healing.describe())
    print(base_healing.attack())
    print(base_healing.heal())
    print(" evolved:")
    evolved_healing = healing_creature.create_evolved()
    print(evolved_healing.describe())
    print(evolved_healing.attack())
    print(evolved_healing.heal())

    print("\nTesting Creature with transform capability")
    print(" base:")
    transform_creature = TransformCreatureFactory()
    base_transform = transform_creature.create_base()
    print(base_transform.describe())
    print(base_transform.attack())
    print(base_transform.transform())
    print(base_transform.attack())
    print(base_transform.revert())
    print(" evolved:")
    evolved_transform = transform_creature.create_evolved()
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(evolved_transform.transform())
    print(evolved_transform.attack())
    print(evolved_transform.revert())


if __name__ == "__main__":
    main()
