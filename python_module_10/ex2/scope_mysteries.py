from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    accumulate = initial_power

    def accum(adding: int) -> int:
        nonlocal accumulate
        accumulate += adding
        return accumulate

    return accum


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def add_item_name(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return add_item_name


def memory_vault() -> dict[str, Callable[..., None | int | str]]:
    vault = {}

    def store(key: str, value: int | str) -> None:
        vault[key] = value

    def recall(key: str) -> int | str:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    try:
        counter_a = mage_counter()
        counter_b = mage_counter()
        accumulate = spell_accumulator(100)
        flaming = enchantment_factory("Flaming")
        frozen = enchantment_factory("Frozen")
        wealth = memory_vault()
        store_wealth = wealth["store"]
        recall_wealth = wealth["recall"]
        print("Testing mage counter...")
        for i in range(1, 4):
            print(f"counter_a call {i}: {counter_a()}")
        for j in range(1, 3):
            print(f"counter_b call {j}: {counter_b()}")
        print()
        print("Testing spell accumulator...")
        print(f"Base 100, add 20: {accumulate(20)}")
        print(f"Base 100, add 30: {accumulate(30)}")
        print()
        print("Testing enchantment factory...")
        print(flaming("Sword"))
        print(frozen("Shield"))
        print()
        print("Testing memory vault...")
        print("Store 'secret' = 42")
        store_wealth("secret", 42)
        print(f"Recall 'secret': {recall_wealth('secret')}")
        print(f"Recall 'unknown': {recall_wealth('unknown')}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
