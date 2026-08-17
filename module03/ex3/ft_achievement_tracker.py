#!/usr/bin/env python3

import random


def missing_achievements(player: str,
                         player_achievements: dict[str, set[str]],
                         achievements: set[str]) -> set[str]:

    return achievements.difference(player_achievements[player])


def unique_achievements(player: str, players: list[str],
                        player_achievements: dict[str, set[str]]) -> set[str]:

    other_players = set()

    for other in players:
        if player != other:
            other_players = other_players.union(player_achievements[other])
    return player_achievements[player].difference(other_players)


def common_achievements(players: list[str],
                        player_achievements: dict[str, set[str]]) -> set[str]:

    common = player_achievements[players[0]]
    for player in players[1:]:
        common = common.intersection(player_achievements[player])
    return common


def distinct_achievements(players: list[str],
                          player_achievements: dict[str, set[str]]
                          ) -> set[str]:

    all_achievements = set()
    for player in players:
        all_achievements = all_achievements.union(
                                player_achievements[player])
    return all_achievements


def gen_player_achievements(achievements: set[str]) -> set[str]:
    number = random.randint(1, len(achievements) - 3)
    return set(random.sample(list(achievements), number))


def main() -> None:
    print("=== Achievement Tracker System ===")
    achievements = {'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer'}
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    player_achievements = {}
    for player in players:
        player_achievements[player] = gen_player_achievements(achievements)
    for player in players:
        print(f"Player {player}: {player_achievements[player]}")
    print(f"\nAll distinct achievements: "
          f"{distinct_achievements(players, player_achievements)}\n")
    print(f"Common achievements: "
          f"{common_achievements(players, player_achievements)}\n")
    for player in players:
        print(f"Only {player} has: "
              f"{unique_achievements(player, players, player_achievements)}")
    print("")
    for player in players:
        missing = missing_achievements(player,
                                       player_achievements,
                                       achievements)
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
