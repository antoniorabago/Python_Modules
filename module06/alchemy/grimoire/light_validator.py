#!/usr/bin/env python3

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for allowed in light_spell_allowed_ingredients():
        if allowed in ingredients.lower():
            return ingredients + "VALID"
    return ingredients + "INVALID"
