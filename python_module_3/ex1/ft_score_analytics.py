# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/19 20:48:24 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/26 14:40:38 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("=== Player Score Analytics ===")


def score_analytics() -> None:
    total_args = len(sys.argv[1:])
    score: list = []
    for arg in sys.argv[1:]:
        try:
            score = score + [int(arg)]
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
    score_analytics()
