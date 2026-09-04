#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        base = Flameling("Flameling", "Fire")
        return base

    def create_evolved(self) -> Creature:
        evolved = Pyrodon("Pyrodon", "Fire/Flying")
        return evolved


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        base = Aquabub("Aquabub", "Water")
        return base

    def create_evolved(self) -> Creature:
        evolved = Torragon("Torragon", "Water")
        return evolved
