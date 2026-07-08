# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 10:49:28 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/22 11:13:51 by tokrabem        ###   ########.fr        #
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
        print(f"{self.name}: {round(self.height, 1)}cm, {self.p_age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    initial_height: float = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        rose.age()
        rose.grow(0.8)
        print(f"=== Day {i} ===")
        rose.show()
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")
    
