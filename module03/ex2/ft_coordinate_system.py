#!/usr/bin/env python3

import math


def distance_to_center(first: tuple[float, float, float],
                       second: tuple[float, float, float] = (0, 0, 0)
                       ) -> float:
    distance = math.sqrt((first[0] - second[0]) ** 2 +
                         (first[1] - second[1]) ** 2 +
                         (first[2] - second[2]) ** 2)
    return distance


def print_coordinates(coordinates: tuple[float, float, float]) -> None:
    print(f"It includes: X={coordinates[0]}, "
          f"Y={coordinates[1]}, Z={coordinates[2]}")


def get_player_pos() -> tuple[float, float, float]:
    while True:
        values = input("Enter new coordinates as floats "
                       "in format 'x,y,z': ").split(",")
        if len(values) != 3:
            print("Invalid syntax")
        else:
            try:
                for value in values:
                    float(value)
                return (float(values[0]), float(values[1]), float(values[2]))
            except ValueError as e:
                print(f"Error on parameter '{value}': {e}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinates1 = get_player_pos()
    print(f"Got a first tuple: {coordinates1}")
    print_coordinates(coordinates1)
    print(f"Distance to center: {distance_to_center(coordinates1):.4f}")
    print("Get a second set of coordinates")
    coordinates2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_to_center(coordinates1, coordinates2):.4f}")


if __name__ == "__main__":
    main()
