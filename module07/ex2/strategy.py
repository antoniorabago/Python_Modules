#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
import typing


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                f"for this aggressive strategy"
            )
        transform_creature = typing.cast(TransformCapability, creature)
        transform_creature.transform()
        print(creature.attack())
        print(transform_creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                f"for this defensive strategy"
            )
        heal_creature = typing.cast(HealCapability, creature)
        print(creature.attack())
        print(heal_creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False


class InvalidStrategyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
