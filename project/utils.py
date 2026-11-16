import os
from pathlib import Path


# fp means filepath
def copy_file(original_fp: str, new_fp: str) -> None:
    """Function to copy a file"""
    with open(original_fp, "rb") as ogf:  # og stands for original, f = file
        with open(new_fp, "wb") as newf:
            for line in ogf:
                newf.write(line)

    os.remove(original_fp)


# We will be taking /home/user/random as example here
def sort_file(original_fp: str) -> None:
    """Sorts the file"""
    original_fp_path = Path(original_fp)  # /home/user/random/hi.txt
    filename = original_fp_path.name  # hi.txt, this is a STRING
    file_ext = Path(filename).suffix  # .txt, this is a STRING

    ext_folder = Path(
        Path(original_fp).parent / str(file_ext).replace(".", "")
    )  # /home/user/random/txt
    ext_folder.mkdir(exist_ok=True)

    new_file = ext_folder / f"{filename}"
    new_file.touch(exist_ok=True)  # /home/user/random/txt/hi.txt

    copy_file(
        original_fp=original_fp,
        new_fp=str(new_file),
    )  # Copies the file from the original destination into the sorted folder
