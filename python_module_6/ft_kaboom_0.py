import alchemy.grimoire


print("=== Kaboom 0 ===")
print("Using grimoire module directly")
name: str = "Fantasy"
ingredients: str = "Earth, wind and fire"
spell_record: str = alchemy.grimoire.light_spell_record(name, ingredients)
validate: str = alchemy.grimoire.validate_ingredients(ingredients)
print(
    f"Testing record light spell: {spell_record} {validate}")
