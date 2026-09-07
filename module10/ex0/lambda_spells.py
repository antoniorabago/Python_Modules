#!/usr/bin/env python3

from data_generator import FuncMageDataGenerator


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    pass


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


def main() -> None:
    artifacts = FuncMageDataGenerator.generate_artifacts(5)

    print("Original artifacts:")
    print(artifacts)

    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))


    print("Testing spell transformer...")


if __name__ == "__main__":
    main()
