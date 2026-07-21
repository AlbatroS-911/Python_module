
def main() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    from alchemy.grimoire.dark_validator import validate_ingredients
    name: str = "Magic potion"
    ingredients: str = "arsenic"
    spell_record: str = dark_spell_record(name, ingredients)
    validate: str = validate_ingredients(ingredients)
    print(
        f"Testing record light spell: {spell_record} {validate}")


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    main()
