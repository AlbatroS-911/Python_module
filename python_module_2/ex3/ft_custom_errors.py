# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/18 14:11:42 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/06 17:43:02 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def raising_all() -> None:
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def catching_all() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught GardenError: {e}")
        print()
    print("Testing PlantError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    raising_all()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    catching_all()
    print("\nAll custom error types correctly!")
