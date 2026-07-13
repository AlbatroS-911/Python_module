# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/27 15:10:33 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/13 22:47:16 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import typing
import sys


def extract_text(filename: str) -> None:
    print(f"Accessing file {filename!r}")
    try:
        fd: typing.IO[str] = open(filename, 'r')
        print(f"---\n\n{fd.read()}\n\n---")
        fd.close()
        print(f"File {filename!r} closed.")
    except Exception as error_opening:
        print(f"Error opening file {filename!r}: {error_opening}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        extract_text(sys.argv[1])
