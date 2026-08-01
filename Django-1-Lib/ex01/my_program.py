#!/usr/bin/env python3
"""
Exercise 01: Pip
Small program using the 'path' library (path.py), installed by my_script.sh
in the local_lib folder.

Authorized module: path (previously called path.py)
"""
from path import Path


def use_path_library():
    """
    Create a folder and a file inside it, write something to that file,
    then read and display its content, all using the Path object from
    the 'path' library.
    """
    folder = Path("my_folder")
    folder.mkdir_p()

    file_path = folder / "my_file.txt"
    file_path.write_text("Hello from the path library!\n")

    content = file_path.read_text()
    print("Content of {}:".format(file_path))
    print(content, end="")


if __name__ == '__main__':
    use_path_library()
