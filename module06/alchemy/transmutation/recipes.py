#!/usr/bin/env python3

from ...elements import create_fire
import alchemy


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{alchemy.create_air()}'" \
           f"and '{alchemy.strength_potion()}' mixed with '{create_fire()}'"
