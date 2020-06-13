import argparse
import gendiff.views as format
from gendiff.diff import generate_diff


def formatter(name):
    if name == format.DEFAULT:
        return format.default
    elif name == format.PLAIN:
        return format.plain
    elif name == format.JSON:
        return format.json


parser = argparse.ArgumentParser()
parser.add_argument("first_file", type=str)
parser.add_argument("second_file", type=str)
parser.add_argument("-f", "--format", default=format.DEFAULT, type=formatter)


def main():
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
