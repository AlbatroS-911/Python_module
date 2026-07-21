from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    list_ingredients: list[str] = dark_spell_allowed_ingredients()
    correct_ingredients = ingredients.replace(",    ", ", ")
    entered_ingredients = correct_ingredients.lower().replace(",", "").split()
    for k in entered_ingredients:
        if k in list_ingredients:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
