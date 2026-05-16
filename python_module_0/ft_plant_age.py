# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_age.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/04/28 16:10:55 by tokrabem          #+#    #+#             #
#    Updated: 2026/04/28 16:15:08 by tokrabem         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
