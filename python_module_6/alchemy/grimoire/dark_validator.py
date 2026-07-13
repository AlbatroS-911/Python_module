from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    list_ingredients: list[str] = dark_spell_allowed_ingredients()
    if ingredients in list_ingredients:
        return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
