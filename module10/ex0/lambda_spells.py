#!/usr/bin/env python3

from data_generator import FuncMageDataGenerator


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: '* ' + spell + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage['power'], mages))
    print(powers)
    return {'max_power': max(mages, key=lambda mage: mage['power'])['power'],
            'min_power': min(mages, key=lambda mage: mage['power'])['power'],
            'avg_power': sum(powers) / len(powers)}


def main() -> None:
    print("Original artifacts:")
    artifacts = FuncMageDataGenerator.generate_artifacts()
    for artifact in artifacts:
        print(artifact)
    print("Testing artifact sorter...")
    artifacts_sorted: list = artifact_sorter(artifacts)
    for artifact in artifacts_sorted:
        print(artifact)

    print("\nOriginal mages:")
    mages = FuncMageDataGenerator.generate_artifacts()
    for mage in mages:
        print(mage)
    print("\nTesting filter mages...")
    mages_filtered: list = power_filter(mages, 100)
    for mage in mages_filtered:
        print(mage)

    print("\nOriginal spells:")
    spells = FuncMageDataGenerator.generate_spells()
    for spell in spells:
        print(spell, end=" ")
    print("\nTesting spell transformer...")
    spells_transformed: list = spell_transformer(spells)
    for spell in spells_transformed:
        print(spell, end=" ")

    print("\n\nOriginal mages:")
    mages = FuncMageDataGenerator.generate_artifacts()
    for mage in mages:
        print(mage)
    print("\nTesting mage stats...")
    mages_stats = mage_stats(mages)
    print(mages_stats)


if __name__ == "__main__":
    main()
