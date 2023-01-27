# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
from dataclasses import dataclass
from typing import Dict

@dataclass
class MinMax:
    min_key: str = ''
    min_counter: int = 0
    max_key: str = ''
    max_counter: int = 0


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
                counter[line] = 1
    return counter


def find_min_max_key(counter: Dict[str, int]) -> MinMax:
    ret = MinMax()
    # find max key
    for k, v in counter.items():
        if ret.max_key == '' or v > ret.max_counter:
            ret.max_key = k
            ret.max_counter = v
        if ret.min_key == '' or v < ret.min_counter:
            ret.min_key = k
            ret.min_counter = v
    return ret


def print_min_max(min_max: MinMax):
    print(f'Min Key = {min_max.min_key} with count = {min_max.min_counter}')
    print(f'Max Key = {min_max.max_key} with count = {min_max.max_counter}')



def main():
    args: argparse.Namespace = parse()
    counter: Dict[str, int] = hist(args)
    min_max: MinMax = find_min_max_key(counter)
    print_min_max(min_max)


if __name__ == '__main__':
    main()
