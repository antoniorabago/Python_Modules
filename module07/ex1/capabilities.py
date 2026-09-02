#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0.factory import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> None:
        ...


class TransformCapability(ABC):
    _transformed: bool = False

    @abstractmethod
    def transform(self) -> None:
        ...

    @abstractmethod
    def revert(self) -> None:
        ...


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def attack(self):
        if not self._transformed:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def revert(self):
        return "Shiftling returns to normal."

    def transform(self):
        self._transformed = True
        return "Shiftling shifts into a sharper form!"


class Morphagon(Creature, TransformCapability):
    def attack(self):
        if not self._transformed:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike"

    def revert(self):
        return "Morphagon stabilizes its form."

    def transform(self):
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        base = Sproutling("Sproutling", "Grass")
        return base

    def create_evolved(self):
        evolved = Bloomelle("Bloomelle", "Grass/Fairy")
        return evolved


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        base = Shiftling("Shiftling", "Normal")
        return base

    def create_evolved(self):
        evolved = Morphagon("Morphagon", "Normal/Dragon")
        return evolved
