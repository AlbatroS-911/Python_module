# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_alchemist.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/27 13:05:37 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/27 15:07:17 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random

print("=== Game Data Alchemist ===")


def fun() -> None:
    players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                          'Gregory', 'john', 'kevin', 'Liam', 'Toky']
    print(f"Initial list of players: {players}")
    capitalized_names: list[str] = []
    only_capitalized: list[str] = []
    capitalized_names = [name.capitalize() for name in players]
    only_capitalized = [name for name in players if name == name.capitalize()]
    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {only_capitalized}")
    score_dict: dict[str, int] = {name: random.randrange(1000)
                                  for name in capitalized_names}
    score_average: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(score_average, 2)}")
    high_score: dict[str, int] = {key: score_dict[key]
                                  for key in score_dict.keys()
                                  if score_dict[key] > score_average}
    print(f"High score: {high_score}")


if __name__ == "__main__":
    fun()
