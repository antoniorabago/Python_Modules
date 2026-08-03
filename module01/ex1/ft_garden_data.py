#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(rose.show())
    print(sunflower.show())
    print(cactus.show())


if __name__ == "__main__":
    main()
