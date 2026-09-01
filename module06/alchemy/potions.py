#!/usr/bin/env python3

import elements
from ..elements import create_fire, create_water


def strength_potion() -> str:
    return f"Strength potion brewed with '{create_fire()}' " \
           f"and '{create_water()}'"


def healing_potion() -> str:
    return f"Healing potion brewed with '{elements.create_earth()}' " \
           f"and '{elements.create_air()}'"
