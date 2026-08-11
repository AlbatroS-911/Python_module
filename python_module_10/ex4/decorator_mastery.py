import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[[str], str]) -> Callable[..., str]:
    @wraps(func)
    def compute_time(*ar: Any, **kw: Any) -> str:
        start_time = time.time()
        result = func(*ar, **kw)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return compute_time


def power_validator(min_power: int) -> Callable[..., Callable[..., str]]:
    def power_decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*ar: Any, **kw: Any) -> str:
            if len(ar) == 1:
                power = ar[0]
            elif len(ar) > 1:
                power = ar[-1]
            elif kw:
                power = kw["power"]
            else:
                power = 0
            if power >= min_power:
                return func(*ar, **kw)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return power_decorator


def retry_spell(max_attempts: int) -> Callable[..., Callable[..., str]]:
    def retry_decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*ar: Any, **kw: Any) -> str:
            if len(ar) == 1:
                power = ar[0]
            elif len(ar) > 1:
                power = ar[-1]
            elif kw:
                power = kw["power"]
            else:
                power = 0
            for attempts in range(1, max_attempts + 1):
                try:
                    if attempts < max_attempts and power < 42:
                        print(
                            "Spell failed, retrying... (attempt "
                            f"{attempts}/{max_attempts})")
                    elif power < 42:
                        return "Spell casting failed after "\
                            f"{max_attempts} attempts"
                    else:
                        return func(*ar, **kw)
                except Exception as e:
                    print(f"Error: {e}")
                power = power + 1
            return ("Spell failed, retrying... (attempt "
                    f"{attempts}/{max_attempts})")
        return wrapper
    return retry_decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 3 and ' ' in name:
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def spread_spell(spell: str) -> str:
        print(f"Casting {spell}...")
        time.sleep(0.1)
        return f"Result: {spell.capitalize()} cast!"

    @power_validator(min_power=30)
    def powering_spell(spell: str, power: int) -> str:
        return f"Enough power({power}) for this spell({spell})."

    @retry_spell(max_attempts=4)
    def fire_spell(spell: str, power: int) -> str:
        return "Waaaaaaagh spelled !"

    try:
        print("Testing spell timer...")
        print(spread_spell("fireball"))
    except Exception as e:
        print(f"Error: {e}")
    print()
    try:
        print("Testing power validator...")
        print(powering_spell("iceball", 42))
    except Exception as e:
        print(f"Error: {e}")
    print()
    try:
        print("Testing retrying spell...")
        print(fire_spell("Fireball", 38))
        print(fire_spell("Fireball", 40))
    except Exception as e:
        print(f"Error: {e}")
    print()
    try:
        print("Testing MageGuild...")
        test_mage: MageGuild = MageGuild()
        print(test_mage.validate_mage_name("Arthur Melo"))
        print(test_mage.validate_mage_name("Gluon"))
        print(test_mage.cast_spell("Lightning", 15))
        print(test_mage.cast_spell("Lightning", 9))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
