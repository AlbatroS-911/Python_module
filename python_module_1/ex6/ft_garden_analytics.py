# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 10:27:07 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/15 21:41:52 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden statistics")


class Plant(object):
    def __init__(self, p_name: str, p_height: float, p_age: int) -> None:
        self.p_name = p_name
        self.p_height = p_height
        self.p_age = p_age

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self.p_name}: Error, age can\'t be negative")
            print("Update rejected")
        else:
            self.p_age = new_age
            print(f"Age updated: {self.p_age} days")

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self.p_name}: Error, height can\'t be negative")
            print("Update rejected")
        else:
            self.p_height = new_height
            print(f"Height updated: {self.p_height}cm")

    def show(self) -> None:
        n, h, a = self.p_name, round(self.p_height, 1), self.p_age
        print(f"{n}: {h}cm, {a} days old")

    @classmethod
    def anonymous(cls) :
        print("\n=== Anonymous")
        cls.p_name, cls.p_height, cls.p_age = "Unknown plant", 0.0, 0
        print(f"{cls.p_name}: {cls.p_height}cm, {cls.p_age} days old")
        print(f"[statistics for {cls.p_name}]")
        print(f"Stats: 0 grow, 0 age, 1 show")

    @staticmethod
    def check_age(age) -> None:
        print("=== Check year-old")
        if (age >= 366):
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")


class Flower(Plant):
    def __init__(self, fn: str, fh: float, fa: int, color: str) -> None:
        super().__init__(fn, fh, fa)
        self.color = color
        self.stat = self.FlowerStat()
        self.__stat = {
                "show" : 0,
                "age" : 0,
                "grow" : 0
            }

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        print(f"{self.p_name} has not bloomed yet")
        self.__stat["show"] += 1

    def age(self, new_age) -> None:
        super().set_age(new_age)
        self.__stat["age"] += 1

    def grow(self, new_height) -> None:
        super().set_height(new_height)
        self.__stat["grow"] += 1

    def bloom(self) -> None:
        print(f"[asking the {self.p_name.lower()} to bloom]")
        super().show()
        print(f"Color: {self.color}")
        print(f"{self.p_name} is blooming beautifully")

    class FlowerStat:
        def __init__(self,  f_name: str) -> None:

        def stat(self) -> None:
            print(f"[statistics for no matter the flower is{self.f_name}...fuuuuckkk]")

    print("\n=== Flower")


if __name__ == "__main__":
    rose = Flower("Rose", 5.0, 10, "Pink")
    rose.show()
    rose.age(0)
    rose.grow(0)
    rose.bloom()
    rose.FlowerStat().stat()