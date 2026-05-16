# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_seed_inventory.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/04/28 19:45:35 by tokrabem          #+#    #+#             #
#    Updated: 2026/04/28 19:45:36 by tokrabem         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
