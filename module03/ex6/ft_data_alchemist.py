#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players: list[str] = ["Alice", "bob", "Charlie", "dylan",
                          "Emma", "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    names_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {names_capitalized}")

    only_capitalized = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")

    scores: dict[str, int] = {name: random.randint(0, 1000)
                              for name in names_capitalized}
    print(f"Score dict: {scores}")

    score_avg = sum(scores.values()) / len(scores)
    print(f"Score average is {score_avg:.2f}")

    above_avg = {name: score
                 for name, score in scores.items()
                 if score > score_avg}
    print(f"High scores: {above_avg}")


if __name__ == "__main__":
    main()
