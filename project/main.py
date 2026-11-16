import sys
from pathlib import Path

import utils


def main() -> None:
    try:
        dir_to_sort: Path = Path(sys.argv[1])
    except IndexError:
        dir_to_sort: Path = Path(
            input("Please enter the dir you want to sort: ")
        )

    for file in Path(dir_to_sort).iterdir():
        if file.is_file():
            utils.sort_file(original_fp=str(file))

    print("Finished sorting!")


if __name__ == "__main__":
    main()
