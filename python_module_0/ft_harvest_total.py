# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tokrabem <tokrabem@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/28 15:25:33 by tokrabem          #+#    #+#              #
#    Updated: 2026/04/28 16:09:01 by tokrabem         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	days = harvest_total = 0
	while (days < 3):
		print(f"Days {days} harvest: ", end = "")
		harvest = int((input()))
		harvest_total += harvest
		days += 1
	print ("Total harvest: ", harvest_total)