#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo === \n")
    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll tests completed - program didn't crash")


if __name__ == "__main__":
    main()
