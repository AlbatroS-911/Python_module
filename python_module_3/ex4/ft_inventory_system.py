# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/26 17:08:21 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/08 07:36:07 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def parse_and_add() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for param in sys.argv[1:]:
        item = param.split(':')
        if len(item) != 2:
            print(f"Error - Invalid parameter {param!r}")
            continue
        key, value = item[0], item[1]
        if not key:
            continue
        if key != key.strip() or value != value.strip():
            print(f"Error - Invalid parameter {param!r}")
            continue
        if key in inventory:
            print(f"Redundant item {key!r} - discarding")
            continue
        try:
            quantity = int(value)
        except ValueError as error:
            print(f"Quantity error for {key!r}: {error}")
            continue
        inventory[key] = quantity
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    print()
    inventory: dict[str, int] = parse_and_add()
    if (inventory):
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        len_dict: int = len(inventory)
        total_quantity: int = sum(list(inventory.values()))
        print(f"Total quantity of {len_dict} items: {total_quantity}")
        for key in inventory:
            percent: float = (inventory[key] / total_quantity) * 100
            print(f"Item {key} represents {round(percent, 1)}%")
        min = list(inventory.keys())[0]
        max = list(inventory.keys())[0]
        for key in inventory.keys():
            if inventory[key] > inventory[max]:
                max = key
            if inventory[key] < inventory[min]:
                min = key
        print(f"Item most abundant: {max} with quantity {inventory[max]}")
        print(f"Item least abundant: {min} with quantity {inventory[min]}")
        inventory.update(magic_item=1)
    else:
        inventory.update(magic_item=1)
    print(f"Updated inventory: {inventory}")
