import argparse
from argparse import Namespace
from unittest import mock

from automated_clean_code.exercise_20_histlib import parse, hist, find_min_max_key, MinMax, print_min_max


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(fname='exercise_20_data.txt'))
def test_parse(mock_args):
    assert isinstance(parse(), Namespace)


def test_hist():
    counter = hist(Namespace(fname='/Users/13am/Desktop/automated-clean-code/tests/exercise_20_data.txt'))
    assert counter['apple'] == 3
    assert counter['banana'] == 2


def test_min_max_key():
    counter = hist(Namespace(fname='/Users/13am/Desktop/automated-clean-code/tests/exercise_20_data.txt'))
    min_max = find_min_max_key(counter)
    assert min_max.max_key == 'apple'
    assert min_max.max_counter == 3
    assert min_max.min_key == 'banana'
    assert min_max.min_counter == 2


def test_print_min_max(capfd):
    min_max = MinMax(min_key='banana', min_counter=2, max_key='apple', max_counter=3)
    print_min_max(min_max)
    out, err = capfd.readouterr()
    assert out == f'Min Key = {min_max.min_key} with count = {min_max.min_counter}\nMax Key = {min_max.max_key} ' \
                  f'with count = {min_max.max_counter}\n'