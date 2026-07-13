# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/02 15:22:38 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/14 00:14:24 by tokrabem        ###   ########.fr        #
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
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        extract_text(sys.argv[1])
        try:
            file = open(f"{sys.argv[1]}", 'r')
            print("Transform data:")
            print("---")
            for line in file:
                new_line = line.strip()
                print(f"{new_line}#")
            print()
            print("---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new_file = sys.stdin.readline().strip()
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
            except (FileNotFoundError, PermissionError) as e:
                print("No saving data", file=sys.stderr)
        except KeyboardInterrupt as f:
            print()
            print("Program interrupted...:", file=sys.stderr)
