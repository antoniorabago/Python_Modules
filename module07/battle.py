#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory


def fight(flame: FlameFactory, aqua: AquaFactory) -> str:
    flame_base = flame.create_base()
    aqua_base = aqua.create_base()
    return (
            f"{flame_base.describe()} \n vs. \n{aqua_base.describe()} \n"
            f" fight!\n{flame_base.attack()}\n{aqua_base.attack()} "
    )


def main() -> None:
    print("Testing factory")
    flame_factory = FlameFactory()
    flame_base = flame_factory.create_base()
    print(flame_base.describe())
    print(flame_base.attack())
    flame_evolved = flame_factory.create_evolved()
    print(flame_evolved.describe())
    print(flame_evolved.attack())

    print("\nTesting factory")
    aqua_factory = AquaFactory()
    aqua_base = aqua_factory.create_base()
    print(aqua_base.describe())
    print(aqua_base.attack())
    aqua_evolved = aqua_factory.create_evolved()
    print(aqua_evolved.describe())
    print(aqua_evolved.attack())

    print("\nTesting battle")
    print(fight(flame_factory, aqua_factory))


if __name__ == "__main__":
    main()
