import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
name: str = "Fantasy"
ingredients: str = "water"
spell_record: str = alchemy.grimoire.light_spell_record(name, ingredients)
validate: str = alchemy.grimoire.validate_ingredients(ingredients)
print(
    f"Testing record light spell: {spell_record} {validate}")
