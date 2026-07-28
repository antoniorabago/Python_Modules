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
    total_growth = 0.0
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.increment_age()
        rose.grow()
        print(rose.show())
    total_growth = rose.height - 25.0
    print(f"Growth this week: {total_growth:.1f}cm")


if __name__ == "__main__":
    main()
