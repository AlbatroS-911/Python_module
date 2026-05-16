# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/04/28 16:30:18 by tokrabem          #+#    #+#             #
#    Updated: 2026/04/28 19:14:25 by tokrabem         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_count_harvest_iterative() -> None:
    harvesting_days = int(input("Days until harvest: "))
    for i in range(1, harvesting_days + 1, 1):
        print("Days ", i)
        i += 1
    print("Harvest time!")
