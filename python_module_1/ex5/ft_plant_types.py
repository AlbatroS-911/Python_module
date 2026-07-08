# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 18:48:11 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/22 12:23:15 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


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


class Flower(Plant):
    def __init__(self, fn: str, fh: float, fa: int, color: str) -> None:
        super().__init__(fn, round(fh, 1), fa)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self._bloomed:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(self, tn: str, th: float, ta: int, trunk_diam: float) -> None:
        self.trunk_diameter = trunk_diam
        super().__init__(tn, round(th, 1), ta)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        n, h, td = self._name, round(self._height, 1), self.trunk_diameter
        print(f"Tree {n} now produces a shade of {h}cm long and {td}cm wide")


class Vegetable(Plant):
    def __init__(self, vn: str, vh: float, va: int, hs: str, nv: int) -> None:
        self.harvest_season = hs
        self.nutritional_value = nv
        super().__init__(vn, round(vh, 1), va)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutrional value : {self.nutritional_value}")

    def grow(self, height_growth: float) -> None:
        self._height = height_growth

    def age(self, age_growth: int) -> None:
        self._age += age_growth
        self.nutritional_value += age_growth


def main() -> None:
    print("=== Garden Plant Types ===")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Flower")
    rose.show()
    print(f"[asking the {rose._name.lower()} to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak.show()
    print(f"[asking the {oak._name.lower()} to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    new_age = 20
    print(f"[make {tomato._name.lower()} grow and age for {new_age} days]")
    tomato.grow(47.0)
    tomato.age(new_age)
    tomato.show()


if __name__ == "__main__":
    main()
