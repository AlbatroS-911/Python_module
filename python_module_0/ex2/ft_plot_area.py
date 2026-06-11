# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plot_area.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/04/28 19:45:35 by tokrabem          #+#    #+#             #
#    Updated: 2026/05/11 06:40:22 by tokrabem         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
