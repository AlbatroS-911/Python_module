import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    OPERATION: list[str] = ["add", "mul", "min", "max"]
    if spells:
        if operation not in OPERATION:
            print(f"Error in operation. Try among these: {OPERATION}")
        else:
            if operation == "add":
                return reduce(operator.add, spells)
            elif operation == "mul":
                return reduce(operator.mul, spells)
            elif operation == "max":
                return reduce(max, spells)
            elif operation == "min":
                return reduce(min, spells)
    return 0


def partial_enchanter(
    base_enchantment: Callable[..., str],
) -> dict[str, Callable[..., str]]:
    return {
        "fireball": partial(base_enchantment, 50, "fireball"),
        "tornado": partial(base_enchantment, 50, "tornado"),
        "earthquake": partial(base_enchantment, 50, "earthquake"),
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Parameter must be a positive number")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(data: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(data: int) -> str:
        return f"Damage spell: {data} damage"

    @dispatcher.register(str)
    def _(data: str) -> str:
        return f"Enchantment: {data}"

    @dispatcher.register(list)
    def _(data: list[str]) -> str:
        return f"Multi-cast: {len(data)} spells"

    return dispatcher


def main() -> None:
    sample_list: list[int] = [2, 3, 4, 5, 6]

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"The {target} is targetted by {element} with {power} power"

    try:
        addition: int = spell_reducer(sample_list, "add")
        multiplication: int = spell_reducer(sample_list, "mul")
        maxi: int = spell_reducer(sample_list, "max")
        mini: int = spell_reducer(sample_list, "min")
        all_enchantement = partial_enchanter(base_enchantment)
        print()
        print("Testing spell reducer...")
        print(f"Sum: {addition}")
        print(f"Product: {multiplication}")
        print(f"Max: {maxi}")
        print(f"Min: {mini}")
        print()
        print("Testing partial enchanter...")
        print(all_enchantement['fireball']('Monster'))
        print(all_enchantement['tornado']('Monster'))
        print(all_enchantement['earthquake']('Monster'))
        print()
        print("Testing memoized fibonacci...")
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
        print()
        print("Testing spell dispatcher...")
        dispatching_test = spell_dispatcher()
        print(dispatching_test(42))
        print(dispatching_test("fireball"))
        print(dispatching_test(["iceball", "fireball", "magic"]))
        print(dispatching_test((1, 2, 3)))
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
