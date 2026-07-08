# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 11:02:04 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/22 11:21:13 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.p_age = age

    def age(self) -> None:
        self.p_age += 1

    def grow(self, growth_index: float) -> None:
        self.height += growth_index

    def show(self) -> None:
        n, h, a = self.name, round(self.height, 1), self.p_age
        print(f"{n}: {h}cm, {a} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose: Plant = Plant("Rose", 25.0, 30)
    oak: Plant = Plant("Oak", 200.0, 365)
    cactus: Plant = Plant("Cactus", 5.0, 90)
    sunflower: Plant = Plant("Sunflower", 80.0, 45)
    fern: Plant = Plant("Fern", 15.0, 120)
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()
