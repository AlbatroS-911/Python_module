# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/20 12:47:51 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/07 22:53:42 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coord = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        try:
            a, b, c = coord.split(',')
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            x = float(a)
        except ValueError as error:
            print(f"Error on parameter {a!r}: {error}")
            continue
        try:
            y = float(b)
        except ValueError as error:
            print(f"Error on parameter {b!r}: {error}")
            continue
        try:
            z = float(c)
        except ValueError as error:
            print(f"Error on parameter {c!r}: {error}")
            continue
        return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    try:
        coord1 = get_player_pos()
        print(f"Got the first tuple: {coord1}")
        x1, y1, z1 = coord1
        print(f"It includes: X={x1}, Y={y1}, Z={z1}")
        print(
            f"Distance to center: "
            f"{round(math.sqrt(x1**2 + y1**2 + z1**2), 4)}")
        print("\nGet a second set of coordinates")
        x2, y2, z2 = get_player_pos()
        dist_pts = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(
            f"Distance between the 2 sets of coordinates: "
            f"{round(dist_pts, 4)}")
    except KeyboardInterrupt:
        print("\nProgram interrupted...")
