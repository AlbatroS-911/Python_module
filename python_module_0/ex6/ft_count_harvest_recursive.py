# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/04/28 16:34:44 by tokrabem          #+#    #+#             #
#    Updated: 2026/04/28 19:06:57 by tokrabem         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_count_harvest_recursive() -> None:
    harvest_days = int(input("Days until harvest: "))

    def count_remaining_days(days):
        if days > harvest_days:
            print("Harvest time!")
            return
        print(f"Day {days}")
        count_remaining_days(days + 1)
    count_remaining_days(1)
