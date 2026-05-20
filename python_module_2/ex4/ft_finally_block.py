# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/19 09:46:12 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/19 18:25:02 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden Watering System ===")


class GardenError(Exception):
    def __init__(self) -> None:
        super().__init__()


class PlantError(GardenError):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return (f"Invalid plant name to water {self.name!r}")


def water_plant(plant_name: str) -> None:
    if (plant_name != plant_name.capitalize()):
        raise PlantError(plant_name)
    print(f"Watering {plant_name}: [OK]")


def test_water_system() -> None:
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PLantError: {error}")
        print("...ending tests and returning to main")
    finally:
        print("Closing water system")
        print("\nCleanup always happens, even with errors!")
    


if __name__ == "__main__":
    test_water_system()
