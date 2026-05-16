# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 14:13:37 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/12 20:25:39 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden Security System ===")


class Plant(object):
    def __init__(self, p_name: str, p_height: float, p_age: int) -> None:
        self.__name = p_name
        self.__height = p_height
        self.__age = p_age

    def get_age(self) -> int:
        if (self.__age < 0):
            return 0
        return 1

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"\n{self.__name}: Error, age can\'t be negative")
            print("Age update rejected")
        else:
            self.__age = new_age
            print(f"\nAge updated: {self.__age} days")

    def get_height(self) -> int:
        if (self.__height < 0):
            return 0
        return 1

    def set_height(self, new_heigth: float) -> None:
        if (new_heigth < 0):
            print(f"{self.__name}: Error, height can\'t be negative")
            print("Height update rejected")
        else:
            self.__height = new_heigth
            print(f"Height update: {self.__height}cm")

    def show(self) -> None:
        n, h, a = self.__name, round(self.__height, 1), self.__age
        print(f"Plant created: {n}: {h}cm, {a} days old")

    def current_state(self) -> None:
        if (self.get_age() and self.get_height()):
            n, h, a = self.__name, round(self.__height, 1), self.__age
            print(f"\nCurrent state: {n}: {h}cm, {a} days old")
        else:
            return


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    rose.set_age(30)
    rose.set_height(25)
    rose.set_age(-9)
    rose.set_height(-5)
    rose.current_state()
