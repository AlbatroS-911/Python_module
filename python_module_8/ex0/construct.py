import sys
import os


def construct() -> None:
    if sys.base_prefix != sys.prefix:
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environement Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting "
              "\nthe global system.")
        print()
        print("Package installation path:")
        for path in sys.path:
            if 'site-packages' in path:
                print(path)

    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env "
              "\nsource matrix_env/bin/activate # On Unix"
              "\nmatrix_env\\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    construct()
