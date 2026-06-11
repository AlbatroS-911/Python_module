# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/02 15:22:38 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/02 18:41:50 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


from typing import IO
import sys


def extract_text(filename: str) -> None:
    print("=== Cyber Archives Recovery && Preservation ===")
    print(f"Accessing file {filename!r}")
    try:
        fd: IO[str] = open(f"{filename}", 'r')
        print(f"---\n\n{fd.read()}\n\n---")
        fd.close()
        print(f"File {filename!r} closed.\n")
    except Exception as e:
        print(
            f"[STDERR] Error opening file {filename!r}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if not sys.argv[1:]:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        extract_text(sys.argv[1])
        try:
            with open(f"{sys.argv[1]}", 'r') as opened_file:
                print("---\n")
                for line in opened_file:
                    new_line = line.strip()
                    print(f"{new_line}#")
                print("\n---")
            new_file = str(input("Enter new file name (or empty): "))
            try:
                opened_file = open(f"{sys.argv[1]}", 'r')
                dest = open(f"{new_file}", 'w')
                for phrase in opened_file:
                    new_phrase = phrase.strip()
                    dest.write(f"{new_phrase}#\n")
                print(f"Saving data to {new_file!r}")
                print(f"Data saved in file {new_file!r}.\n")
                opened_file.close()
                dest.close()
            except Exception as e:
                print(
                    f"[STDERR] Error opening file {new_file!r}: {e}", file=sys.stderr)
        except BaseException:
            print("No saving data.")
