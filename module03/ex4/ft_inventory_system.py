#!/usr/bin/env python3

import sys


def get_min(inventory: dict[str, int]) -> tuple[str, int]:
    keys = list(inventory.keys())
    min_key = keys[0]
    min_value = inventory[min_key]
    for key in keys[1:]:
        if inventory[key] < min_value:
            min_key = key
            min_value = inventory[key]
    return (min_key, min_value)


def get_max(inventory: dict[str, int]) -> tuple[str, int]:
    max_key: str = ""
    max_value: int = 0

    for key in inventory.keys():
        if inventory[key] > max_value:
            max_key = key
            max_value = inventory[key]
    return (max_key, max_value)


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value = arg.split(":")
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} "
          f"items: {total_quantity}")

    if inventory:
        for key in inventory.keys():
            key_value = inventory[key]
            print(f"Item {key} represents "
                  f"{(key_value/total_quantity) * 100:.1f}%")

        max_key, max_value = get_max(inventory)
        print(f"Item most abundant: {max_key} "
              f"with quantity {max_value}")
        min_key, min_value = get_min(inventory)
        print(f"Item least abundant: {min_key} "
              f"with quantity {min_value}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
