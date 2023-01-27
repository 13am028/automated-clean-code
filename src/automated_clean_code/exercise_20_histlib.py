# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
from typing import Dict


def parse():
    parser = argparse.ArgumentParser(
        description='compute the entry with the most occurrence and the least occurrence form a file')
    parser.add_argument('fname', metavar='N', type=str,
                        help='filename to compute the histogram')
    return parser.parse_args()


def hist(args: argparse.Namespace) -> Dict[str, int]:
    counter = {}
    # fill up histogram
    with open(args.fname, 'r') as f:
        for line in f:
            line = line.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 0
    return counter


def find_min_max_key(counter: Dict[str, int]) -> (str, int, str, int):
    max_key: str = ''
    max_counter: int = 0
    min_key: str = ''
    min_counter: int = 0
    # find max key
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v + 1
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v + 1
    return min_key, min_counter, max_key, max_counter


def main():
    args: argparse.Namespace = parse()
    counter: Dict[str, int] = hist(args)
    min_key, min_counter, max_key, max_counter = find_min_max_key(counter)
    print(f'Min Key = {min_key} with count = {min_counter}')
    print(f'Max Key = {max_key} with count = {max_counter}')


if __name__ == '__main__':
    main()
