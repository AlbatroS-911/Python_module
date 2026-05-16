# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_water_reminder.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/04/28 16:22:37 by tokrabem          #+#    #+#             #
#    Updated: 2026/04/28 19:18:43 by tokrabem         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_water_reminder() -> None:
    not_watered = int(input("Days since last watering: "))
    if (not_watered > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
