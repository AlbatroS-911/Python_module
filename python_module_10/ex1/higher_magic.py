from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        print(f"Original: {power}, Amplified: {power * multiplier}")
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
        condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    def list_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return list_spell


def main() -> None:
    try:

        def fireball(target: str, power: int) -> str:
            return f"{target} hitted by {power} power of fireball"

        def heal(target: str, power: int) -> str:
            return f"Heal restores {target} for {power} HP"

        def original_spell(target: str, power: int) -> str:
            return f"{power} fire damage to {target} with amplifier"

        def condition(target: str, power: int) -> bool:
            return target in ["Zombie", "Vampire", "Werewolf"] and power > 49

        def spell_execution(target: str, power: int) -> str:
            return f"Spell hits {target} with {power} power"

        combined = spell_combiner(fireball, heal)
        test_combined = combined("Dragon", 100)
        amplified_spell = power_amplifier(original_spell, 10)
        test_condition = conditional_caster(condition, spell_execution)
        test_list_callable = spell_sequence([fireball, heal, original_spell])
        print("Testing spell combiner...")
        print(f"Combined spell result: {test_combined[0]}, {test_combined[1]}")
        print()
        print("Testing power amplifier...")
        print(amplified_spell("Dragon", 10))
        print()
        print("Testing conditionnal caster...")
        print("Testing valid condition...")
        print(test_condition("Vampire", 50))
        print("Testing invalid condition...")
        print(test_condition("Dragon", 50))
        print()
        print("Testing spell sequence...")
        print(*test_list_callable("Cannibal", 50), sep="\n")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
