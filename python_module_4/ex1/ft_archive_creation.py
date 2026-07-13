import typing
import sys


def extract_text(filename: str) -> None:
    print("=== Cyber Archives Recovery && Preservation ===")
    print(f"Accessing file {filename!r}")
    try:
        fd: typing.IO[str] = open(filename, 'r')
        print(f"---\n\n{fd.read()}\n\n---")
        fd.close()
        print(f"File {filename!r} closed.\n")
    except Exception as error_opening:
        print(f"Error opening file {filename!r}: {error_opening}")


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
            except (FileNotFoundError, PermissionError):
                print("No saving data")
        except KeyboardInterrupt:
            print()
            print("Program interrupted...")
