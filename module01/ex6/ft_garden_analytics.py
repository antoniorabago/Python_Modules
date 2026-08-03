#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int
    _grow_rate: float

    class Statistics:
        _grow_stat: int
        _age_stat: int
        _show_stat: int

        def __init__(self) -> None:
            self._grow_stat = 0
            self._age_stat = 0
            self._show_stat = 0

        def grow(self) -> None:
            self._grow_stat += 1

        def increment_age(self) -> None:
            self._age_stat += 1

        def show(self) -> None:
            self._show_stat += 1

        def stats(self) -> str:
            return (
                f"{self._grow_stat} grow, {self._age_stat} age, "
                f"{self._show_stat} show"
            )

    def __init__(self, name: str, height: float,
                 age: int, grow_rate: float) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self._grow_rate = grow_rate

        self.set_height(height)
        self.set_age(age)
        self._stats = Plant.Statistics()

    def show(self) -> str:
        self._stats.show()
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"

    def increment_age(self, days: int = 1) -> None:
        self._stats.increment_age()
        self._age += days

    def grow(self) -> None:
        self._stats.grow()
        self._height += self._grow_rate

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

    @staticmethod
    def older(age: int) -> str:
        if age <= 365:
            return f"Is {age} days more than a year? -> False"
        else:
            return f"Is {age} days more than a year? -> True"

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def stats(self) -> str:
        return self._stats.stats()


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
        if self._bloom:
            return f" {self._name} is blooming beautifully!"
        else:
            return f" {self._name} has not bloomed yet"

    def show(self) -> str:
        return f"{super().show()} \n Color: {self._color}"


class Tree(Plant):
    _trunk_diameter: float

    class TreeStatistics(Plant.Statistics):
        _shade_stat: int

        def __init__(self) -> None:
            super().__init__()
            self._shade_stat = 0

        def produce_shade(self) -> None:
            self._shade_stat += 1

        def stats(self) -> str:
            return (
                f"{super().stats()}\n"
                f" {self._shade_stat} shade"
            )

    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, grow_rate)
        self._trunk_diameter = trunk_diameter
        self._tree_stats = Tree.TreeStatistics()
        self._stats = self._tree_stats

    def produce_shade(self) -> str:
        self._tree_stats.produce_shade()
        return (
            f"Tree {self._name} now produces a shade of {self._height}cm long "
            f"and {self._trunk_diameter}cm wide."
        )

    def show(self) -> str:
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
        return (
            f"{super().show()} \n Harvest season: {self._harvest_season} \n"
            f" Nutritional value: {self._nutritional_value}"
        )


class Seed(Flower):
    _seeds_number: int

    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float, color: str, seeds_number: int) -> None:
        super().__init__(name, height, age, grow_rate, color)
        self._seeds_number = seeds_number

    def set_seed_number(self, seed_number: int) -> None:
        self._seeds_number = seed_number

    def get_seed_number(self) -> int:
        return self._seeds_number

    def show(self) -> str:
        return (
            f"{super().show()} \n{super().is_blooming()} \n "
            f"Seeds: {self._seeds_number}"
        )

    def bloom(self, seed_number: int = 0) -> None:
        super().bloom()
        self.set_seed_number(seed_number)


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    print(f"Stats: {plant.stats()}")


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(Plant.older(30))
    print(Plant.older(400))

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    print(rose.show())
    print(rose.is_blooming())
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    print(rose.show())
    print(rose.is_blooming())
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    print(oak.show())
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow", 0)
    print(sunflower.show())
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.increment_age(20)
    sunflower.bloom(42)
    print(sunflower.show())
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    print(unknown.show())
    display_statistics(unknown)


if __name__ == "__main__":
    main()
