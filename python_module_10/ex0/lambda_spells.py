from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not artifacts:
        raise Exception("List should not empty")
    sorted_dict: list[dict[str, Any]] = sorted(
        artifacts, key=lambda x: x["power"], reverse=True
    )
    return sorted_dict


def power_filter(mages: list[dict[Any, Any]],
                 min_power: int) -> list[dict[str, str]]:
    if not mages:
        raise Exception("List should not empty")
    filtered_list: list[dict[Any, Any]] = list(
        filter(lambda x: x["power"] >= min_power, mages)
    )
    return filtered_list


def spell_transformer(spells: list[str]) -> list[str]:
    if not spells:
        raise Exception("List should not empty")
    transformed_str: list[str] = list(map(lambda x: "* " + x + " *", spells))
    return transformed_str


def mage_stats(mages: list[dict[Any, Any]]) -> dict[str, Any]:
    if not mages:
        raise Exception("List should not empty")
    try:
        powers = [m["power"] for m in mages]
        return {
            "min_power": min(mages, key=lambda c: c["power"])["power"],
            "max_power": max(mages, key=lambda c: c["power"])["power"],
            "avg_power": round(sum(powers) / len(powers), 2),
        }
    except KeyError as er:
        print(f"Missing key {er}")
        raise


if __name__ == "__main__":

    sample: list[dict[str, Any]] = [
        {"name": "Vehicle", "power": 25, "type": "auto"},
        {"name": "Truck", "power": 240, "type": "auto"},
        {"name": "Mini-bus", "power": 68, "type": "auto"},
        {"name": "RocketShip", "power": 250, "type": "auto"},
    ]
    original_str: list[str] = ["fireball", "heal", "shield"]
    try:
        sorted_artifact: list[dict[str, Any]] = artifact_sorter(sample)
        print("Testing artifact sorter...")
        print(
            f"{sorted_artifact[0]['name']} ("
            f"{sorted_artifact[0]['power']} power)",
            end="",
        )
        for i in range(1, len(sorted_artifact)):
            print(
                f"comes before {sorted_artifact[i]['name']}"
                f" ({sorted_artifact[i]['power']} power) ",
                end="",
            )
        print("\n")
    except Exception as e:
        print(f"Error, invalid data structure: {e}")
        print()
    try:
        filtered_list: list[dict[str, str]] = power_filter(sample, 20)
        print("Testing power filter...")
        print("The list that belong to the filter:")
        for i in range(len(filtered_list)):
            print(
                f"{filtered_list[i]['name']}: ("
                f"{filtered_list[i]['power']}) power")
        print()
    except Exception as e:
        print(f"Error, invalid data structure: {e}")
        print()
    try:
        trans_str: list[str] = spell_transformer(original_str)
        print("Testing spell transformed...")
        print(*trans_str)
        print()
    except Exception as e:
        print(f"Error, invalid data structure: {e}")
        print()
    try:
        stat: dict[str, Any] = mage_stats(sample)
        print("Testing mages stats...")
        print(f"Max power level: ({stat['max_power']} power)")
        print(f"Min power level: ({stat['min_power']} power)")
        print(f"Average power level: ({stat['avg_power']})")
    except Exception as e:
        print(f"Error, invalid data structure: {e}")
        print()
