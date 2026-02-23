import sys
import os
import re
import settings


def main():
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Error")
        return

    filename = sys.argv[1]

    # Check extension
    if not filename.endswith(".template"):
        print("Error")
        return

    # Check if file exists
    if not os.path.isfile(filename):
        print("Error")
        return

    # Read template file
    try:
        with open(filename, "r") as f:
            content = f.read()
    except:
        print("Error")
        return

    # Replace variables
    try:
        content = content.format(**vars(settings))
    except:
        print("Error")
        return

    # Create output file
    output_file = filename.replace(".template", ".html")

    # Write result
    try:
        with open(output_file, "w") as f:
            f.write(content)
    except:
        print("Error")
        return


if __name__ == "__main__":
    main()
