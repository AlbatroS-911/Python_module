# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/11 18:48:11 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/12 19:48:19 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden Plant Types ===")


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

    def show(self) -> None:
        print("\n=== Flower")
        super().show()
        print(f"Color: {self.color}")
        print(f"{self.p_name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.p_name.lower()} to bloom]")
        super().show()
        print(f"Color: {self.color}")
        print(f"{self.p_name} is blooming beautifully")


class Tree(Plant):
    def __init__(self, tn: str, th: float, ta: int, trunk_diam: float) -> None:
        self.trunk_diameter = trunk_diam
        super().__init__(tn, round(th, 1), ta)

    def show(self) -> None:
        print("\n=== Tree")
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        n, h, td = self.p_name, round(self.p_height, 1), self.trunk_diameter
        print(f"[asking the {n.lower()} to produce shade]")
        print(f"Tree {n} now produces a shade of {h}cm long and {td}cm wide")


class Vegetable(Plant):
    def __init__(self, vn: str, vh: float, va: int, hs: str, nv: int) -> None:
        self.harvest_season = hs
        self.nutritional_value = nv
        super().__init__(vn, round(vh, 1), va)

    def show(self) -> None:
        print("\n=== Vegetable")
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrional value : {self.nutritional_value}")

    def grow(self, height_growth: float, age_growth: int) -> None:
        n = self.p_name
        print(f"[make {n.lower()} grow and age for {age_growth} days]")
        self.p_height = height_growth
        final_age = self.p_age + age_growth
        for i in range(self.p_age, final_age):
            self.nutritional_value += 1
        self.p_age = final_age
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrional value : {self.nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    rose.show()
    rose.bloom()
    oak.show()
    oak.produce_shade()
    tomato.show()
    tomato.grow(47.0, 20)
