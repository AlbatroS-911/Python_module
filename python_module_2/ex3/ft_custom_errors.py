# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/18 14:11:42 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/19 13:55:37 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Custom Garden Errors Demo ===")

class GardenError(Exception):
    def __init__(self, message: str = "Garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str, mess: str = "Unknown plant error") -> None:  
        super().__init__(mess)  
        self.name = name
        self.message = mess
    
    def __str__ (self) -> str:
        if (self.name):
            return (f"The {self.name} plant is wilting!")
        else:
            return self.message
    

class WaterError(GardenError):
    def __init__(self, temp: int, mess: str = "Unknown water error") -> None:
        super().__init__(mess)
        self.temp = temp
        self.message = mess

    def __str__(self) -> str:
        if (self.temp > 20):
            return (self.message)
        else:
            return "Not enough water in the tank!"


def raising_plant_error() -> None:
    print("\nTesting PlantError...")
    raise PlantError("tomato")

def raising_water_error() -> None:
    print("\nTesting water error...")
    raise WaterError(15)

def raising_all() -> None:
    print("\nTesting all garden errors...")
    try:
        raise PlantError("tomato")
    except PlantError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError(15)
    except WaterError as e:
        print(f"Caught GardenError: {e}")
        

def catching_error() -> None:
    try:
        raising_plant_error()
    except PlantError as plant_error:
        print(f"Caught PlantError: {plant_error}")
    try:
        raising_water_error()
    except WaterError as water_error:
        print(f"Caught WaterError: {water_error}")
    raising_all()
    print("\nAll custom error types correctly!")

if __name__ == "__main__":
    catching_error()