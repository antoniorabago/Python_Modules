#!/usr/bin/env python3

import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    record = alchemy.grimoire.light_spell_record(
        'Fantasy',
        'Earth, wind and fire'
    )
    print(f"Testing record light spell: {record}")


if __name__ == "__main__":
    main()
