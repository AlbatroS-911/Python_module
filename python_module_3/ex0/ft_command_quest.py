# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/19 18:27:09 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/07 21:15:38 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def count_arguments() -> None:
    total_args: int = len(sys.argv)

    print(f"Program name : {sys.argv[0]}")
    if (total_args <= 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")
        for i in range(1, total_args):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    count_arguments()
