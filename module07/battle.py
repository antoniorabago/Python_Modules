#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> str:
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    return (
            f"{base1.describe()} \n vs. \n{base2.describe()} \n"
            f" fight!\n{base1.attack()}\n{base2.attack()} "
    )


def main() -> None:
    flame_factory = FlameFactory()
    test_factory(flame_factory)
    print()
    aqua_factory = AquaFactory()
    test_factory(aqua_factory)

    print("\nTesting battle")
    print(fight(flame_factory, aqua_factory))


if __name__ == "__main__":
    main()
