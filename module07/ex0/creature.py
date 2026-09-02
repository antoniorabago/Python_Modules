#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    _name: str = ""
    _type: str = ""

    @abstractmethod
    def attack() -> None:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
