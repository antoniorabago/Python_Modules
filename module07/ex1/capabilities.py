#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0.factory import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):
    _transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def attack(self) -> str:
        if not self._transformed:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} performs a boosted strike!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"


class Morphagon(Creature, TransformCapability):
    def attack(self) -> str:
        if not self._transformed:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} unleashes a devastating morph strike!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        base = Sproutling("Sproutling", "Grass")
        return base

    def create_evolved(self) -> Bloomelle:
        evolved = Bloomelle("Bloomelle", "Grass/Fairy")
        return evolved


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        base = Shiftling("Shiftling", "Normal")
        return base

    def create_evolved(self) -> Morphagon:
        evolved = Morphagon("Morphagon", "Normal/Dragon")
        return evolved
