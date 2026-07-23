class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def increment_age(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height += 0.8

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = height
        else:
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self._age = age
        else:
            print("Age update rejected")

    def get_height(self) -> None:
        return f"{self._height:.1f}"

    def get_age(self) -> None:
        return f"{self._age}"


def main() -> None:
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:")

if __name__ == "__main__":
    main()
