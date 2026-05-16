# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_data.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/05/11 08:36:23 by tokrabem          #+#    #+#             #
#    Updated: 2026/05/11 08:36:24 by tokrabem         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

class Plant:
    def __init__(self, plant_name: str, plant_height: int, plant_age: int) -> None:
        self.name = plant_name
        self.height = plant_height
        self.age = plant_age

    def show(self) -> None:
        print(f"{self.name} : {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
