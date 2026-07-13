from .light_validator import validate_ingredients
# import light_validator


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    
    if validate_ingredients(ingredients):
        return f"Spell recorded: {spell_name}"
    return f"Spell rejected: {spell_name}"
