#!/usr/bin/env python3

import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: Recipe transmuting Lead to Gold: "
          f"brew '{create_air()}' and '{strenght_potion()} "
          f"")


if __name__ == "__main__":
    main()
