class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def show(self) -> str:
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"

    def increment_age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height += 0.8

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name} Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f"{self._name} Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name


def main() -> None:
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:", rose.show())
    rose.set_height(25)
    print(f"\nHeight updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days\n")
    rose.set_height(-3)
    rose.set_age(-5)
    print("\nCurrent state:", rose.show())


if __name__ == "__main__":
    main()
