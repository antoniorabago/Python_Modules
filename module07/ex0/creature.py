#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    _name: str = ""
    _creature_type: str = ""

    def __init__(self, name: str, creature_type: str) -> None:
        self._name = name
        self._creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._creature_type} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"
