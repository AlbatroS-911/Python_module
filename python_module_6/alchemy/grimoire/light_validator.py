


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    list_ingredients: list[str] = light_spell_allowed_ingredients()
    if ingredients in list_ingredients:
        return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
