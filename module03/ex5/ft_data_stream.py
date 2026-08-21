#!/usr/bin/env python3

import random
from typing import Generator


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def gen_event(players: list[str],
              actions: list[str]) -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield player, action


def main() -> None:
    print("=== Game Data Stream Processor ===")
    players: list[str] = ["bob", "alice", "dylan", "charlie"]
    actions: list[str] = ["run", "eat", "sleep", "grab",
                          "move", "climb", "swim"]
    events: list[tuple[str, str]] = []

    generator = gen_event(players, actions)

    for event_number in range(1000):
        event = next(generator)
        print(f"Event {event_number}: Player {event[0]} "
              f"did action {event[1]}")

    for _ in range(10):
        events.append(next(generator))
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
