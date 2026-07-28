class Plant:
    _name: str
    _height: float
    _age: int
    _grow_rate: float

    def __init__(self, name: str, height: float,
                 age: int, grow_rate: float) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self._grow_rate = grow_rate

        self.set_height(height)
        self.set_age(age)

    def show(self) -> str:
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"

    def increment_age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height += self._grow_rate

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = height
        else:
            print(f"{self._name} Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self._age = age
        else:
            print(f"{self._name} Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> str:
        return f"{self._height}"

    def get_age(self) -> str:
        return f"{self._age}"


class Flower(Plant):
    _color: str
    _bloom: bool

    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float, color: str) -> None:
        super().__init__(name, height, age, grow_rate)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        self._bloom = True

    def is_blooming(self) -> str:
        if (self._bloom):
            return " Rose is blooming beautifully!"
        else:
            return " Rose has not bloomed yet"

    def show(self) -> str:
        return f"{super().show()} \n Color: {self._color}"


class Tree(Plant):
    _trunk_diameter: float

    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, grow_rate)
        self._trunk_diameter = trunk_diameter
        self._shade = False

    def produce_shade(self) -> str:
        return (
            f"Tree Oak now produces a shade of {self._height}cm long "
            f"and {self._trunk_diameter}cm wide."
        )

    def show(self) -> str:
        super().show()
        return f"{super().show()} \n Trunk diameter: {self._trunk_diameter}cm"


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float, harvest_season: str) -> None:
        super().__init__(name, height, age, grow_rate)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = 0

    def grow(self) -> None:
        super().increment_age()
        super().grow()
        self._nutritional_value += 1

    def show(self) -> str:
        super().show()
        return (
            f"{super().show()} \n Harvest season: {self._harvest_season} \n"
            f" Nutritional value: {self._nutritional_value}"
        )


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.8, "red")
    print(rose.show())
    print(rose.is_blooming())
    print("[asking the rose to bloom]")
    rose.bloom()
    print(rose.show())
    print(rose.is_blooming())

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    print(oak.show())
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    print(tomato.show())
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
    print(tomato.show())


if __name__ == "__main__":
    main()
