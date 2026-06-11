# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 10:27:07 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/11 13:12:01 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant(object):
    def __init__(self, name: str, height: float, age: int) -> None:
        self.p_name = name
        self.p_height = height
        self.p_age = age

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            return
        else:
            self.p_age = new_age

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            return
        else:
            self.p_height = new_height

    def show(self) -> None:
        n, h, a = self.p_name, round(self.p_height, 1), self.p_age
        print(f"{n}: {h}cm, {a} days old")

    @classmethod
    def anonymous(cls) -> None:
        print("\n=== Anonymous")
        name, height, age = "Unknown plant", 0.0, 0
        print(f"{name}: {height}cm, {age} days old")
        print(f"[statistics for {name}]")
        print("Stats: 0 grow, 0 age, 1 show")

    @staticmethod
    def check_age(age: int) -> bool:
        output = age > 365
        print(f"Is {age} days more than a year? -> {output}")
        return output


class Flower(Plant):

    class FlowerStat:
        def __init__(self, name: str) -> None:
            self.name = name
            self.grow = 0
            self.age = 0
            self.show = 0
            self.shade = 0

    def __init__(self, fn: str, fh: float, fa: int, color: str) -> None:
        super().__init__(fn, fh, fa)
        self.color = color
        self._bloomed = False
        self._stat = self.FlowerStat(fn)

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self._bloomed:
            print(f" {self.p_name} has not bloomed yet")
        else:
            print(f" {self.p_name} is blooming beautifully")
        self._stat.show += 1

    def age(self, new_age: int) -> None:
        super().set_age(new_age)
        self._stat.age += 1

    def grow(self, new_height: float) -> None:
        super().set_height(new_height)
        self._stat.grow += 1

    def bloom(self) -> None:
        self._bloomed = True


class Seed(Flower):
    def __init__(self, fn: str, fh: float, fa: int, color: str) -> None:
        super().__init__(fn, fh, fa, color)
        self.seed = 0

    def show(self) -> None:
        super().show()
        if self._bloomed:
            self.seed = 42
        print(f" Seeds: {self.seed}")


class Tree(Plant):
    class TreeStat:
        def __init__(self, name: str) -> None:
            self.name = name
            self.grow = 0
            self.age = 0
            self.show = 0
            self.shade = 1

    def __init__(self, tn: str, th: float, ta: int, td: float) -> None:
        super().__init__(tn, th, ta)
        self.trunk_diam = round(td, 1)
        self._stat = self.TreeStat(tn)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diam}cm")
        self._stat.show += 1

    def age(self, new_age: int) -> None:
        super().set_age(new_age)
        self._stat.age += 1

    def grow(self, new_height: float) -> None:
        super().set_height(new_height)
        self._stat.grow += 1

    def shade(self) -> None:
        print(
            f"Tree {self.p_name} now produces a shade of {self.p_height}cm"
            f" long and {self.trunk_diam}cm wide."
        )
        self._stat.shade += 1


def display_stat(stat: Flower.FlowerStat | Tree.TreeStat) -> None:
    print(f"[statistics for {stat.name}]")
    print(f"Stats: {stat.grow} grow, {stat.age} age, {stat.show} show")
    if stat.shade:
        print(f" {stat.shade - 1} shade")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "Red")
    rose.show()
    display_stat(rose._stat)
    print(f"[asking the {rose.p_name.lower()} to grow and bloom]")
    rose.grow(23.0)
    rose.bloom()
    rose.show()
    display_stat(rose._stat)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stat(oak._stat)
    print(f"[asking the {oak.p_name.lower()} to produce shade]")
    oak.shade()
    display_stat(oak._stat)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(110.0)
    sunflower.age(65)
    sunflower.bloom()
    sunflower.show()
    display_stat(sunflower._stat)
    Plant.anonymous()


if __name__ == "__main__":
    main()
