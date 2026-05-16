#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 10:49:28 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/11 13:58:01 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, p_name: str, p_height: float, p_age: int) -> None:
        self.name = p_name
        self.height = p_height
        self.p_age = p_age

    def age(self) -> None:
        self.p_age += 1

    def grow(self, growth_index: float) -> None:
        self.height += growth_index

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.p_age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", round(25.0, 1), 30)
    initial_height: float = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8, 1):
        rose.age()
        rose.grow(0.8)
        print(f"=== Day {i} ===")
        rose.show()
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")
