#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def increment_age(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height += 0.8


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    print("Created:", rose.show())
    oak = Plant("Oak", 200.0, 365)
    print("Created:", oak.show())
    cactus = Plant("Cactus", 5.0, 90)
    print("Created:", cactus.show())
    sunflower = Plant("Sunflower", 80.0, 45)
    print("Created:", sunflower.show())
    fern = Plant("Fern", 15.0, 120)
    print("Created:", fern.show())


if __name__ == "__main__":
    main()
