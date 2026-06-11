# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 11:02:04 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/11 12:58:08 by tokrabem        ###   ########.fr        #
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
        print(f"Created: {n}: {h}cm, {a} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
