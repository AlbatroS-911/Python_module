

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    list_ingredients: list[str] = light_spell_allowed_ingredients()
    correct_ingredients = ingredients.replace(",    ", ", ")
    entered_ingredients = correct_ingredients.lower().replace(",", "").split()
    for k in entered_ingredients:
        if k in list_ingredients:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
