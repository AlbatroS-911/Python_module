# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 18:48:11 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/11 18:10:59 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant(object):
    def __init__(self, p_name: str, p_height: float, p_age: int) -> None:
        self.p_name = p_name
        self.p_height = p_height
        self.p_age = p_age

    def show(self) -> None:
        n, h, a = self.p_name, round(self.p_height, 1), self.p_age
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
            print(f" {self.p_name} has not bloomed yet")
        else:
            print(f" {self.p_name} is blooming beautifully")

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
        n, h, td = self.p_name, round(self.p_height, 1), self.trunk_diameter
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
        self.p_height = height_growth

    def age(self, age_growth: int) -> None:
        self.p_age += age_growth
        self.nutritional_value += age_growth


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Flower")
    rose.show()
    print(f"[asking the {rose.p_name.lower()} to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak.show()
    print(f"[asking the {oak.p_name.lower()} to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    new_age = 20
    print(f"[make {tomato.p_name.lower()} grow and age for {new_age} days]")
    tomato.grow(47.0)
    tomato.age(new_age)
    tomato.show()


if __name__ == "__main__":
    main()
