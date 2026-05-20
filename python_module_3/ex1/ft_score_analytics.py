# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/19 20:48:24 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/20 07:04:27 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("=== Player Score Analytics ===")


def score_analytics() -> None:
    score: list = []
    print(len(sys.argv))
    for i in range(1, len(sys.argv)):
        score += sys.argv[i]
    print(f"Scores processed: {score}")
    print(type(score[0]))


if __name__ == "__main__":
    score_analytics()