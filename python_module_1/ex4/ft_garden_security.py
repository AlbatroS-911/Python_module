# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 14:13:37 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/22 11:52:54 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden Security System ===")


class Plant(object):
    def __init__(self, p_name: str, p_height: float, p_age: int) -> None:
        self._name = p_name
        self._height = 0.0
        self._age = 0
        if p_age < 0:
            print("Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = p_age
        if p_height < 0:
            print("Error, height can't be negative")
            print("Age update rejected")
        else:
            self._height = p_height

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_heigth: float) -> None:
        if (new_heigth < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_heigth
            print(f"Height update: {self._height}cm")

    def show(self) -> None:
        n, h, a = self._name, round(self._height, 1), self._age
        print(f"{n}: {h}cm, {a} days old")

    def current_state(self) -> None:
        n, h, a = self._name, round(self._height, 1), self._age
        print(f"Current state: {n}: {h}cm, {a} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 15.0, 10)
    print("Plant created:", end="")
    rose.show()
    print("\n", end="")
    rose.set_age(30)
    rose.set_height(25)
    print("\n", end="")
    rose.set_age(-9)
    rose.set_height(-5)
    print("\n", end="")
    rose.current_state()
