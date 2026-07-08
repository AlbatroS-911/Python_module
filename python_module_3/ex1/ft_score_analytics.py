# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/19 20:48:24 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/07 21:44:28 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def score_analytics() -> None:
    total_args: int = 0
    score: list[int] = []
    for arg in sys.argv[1:]:
        try:
            score += [int(arg)]
            total_args += 1
        except ValueError:
            print(f"Invalid parameter: {arg!r}")
    if (total_args == 0):
        print("No score provided."
              f" Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        print(f"Scores processed: {score}")
        print(f"Total players: {total_args}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {round(sum(score) / total_args, 1)}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
