import argparse
import glob
import os
import pathlib
from collections import namedtuple

Options = namedtuple("Options", "path, name, print")


def main() -> int:
    """Entry point for find_cmd."""
    parser = argparse.ArgumentParser(
        "find",
        description="walk a file hierarchy",
        usage="%(prog)s path ... -name pattern -print")

    parser.add_argument(
        "path",
        action="store")

    parser.add_argument(
        "-name",
        required=True,
        action="store",
        help="Match the last component of the pathname.")

    parser.add_argument(
        "-print",
        required=True,
        action="store_true",
        help="Print the pathname of the current file to standard output.")

    options = Options(**vars(parser.parse_args()))

    for dir_path, _, _ in os.walk(options.path):
        for path_name in glob.iglob(options.name, root_dir=dir_path):
            if options.print:
                print(pathlib.Path(dir_path, path_name))

    return 0
