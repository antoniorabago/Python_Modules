#!/usr/bin/env python3

from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Spell restores {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return (spell1, spell2)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable[[int], int]:
    def amplified(multiplier: int) -> int:
        return spell(base_spell * multiplier)
    return amplified


# def conditional_caster(condition: Callable, spell: Callable) -> Callable:
#     pass


# def spell_sequence(spells: list[Callable]) -> Callable:
#     pass


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined)

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)

    print("Testing conditional caster...")

    print("Testing spell sequence...")


if __name__ == "__main__":
    main()


# === Exercise 1 Test Data ===
# # Higher Realm Test Data
# # Use these in your test functions:
# test_values = [7, 16, 5]
# test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
