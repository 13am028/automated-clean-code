from argparse import Namespace

from automated_clean_code.exercise_20_histlib import hist, find_min_max_key


def test_min_max_key():
    counter = hist(Namespace(fname='exercise_20_data.txt'))
    min_key, min_counter, max_key, max_counter = find_min_max_key(counter)
    assert max_key == 'apple'
    assert max_counter == 3
    assert min_key == 'banana'
    assert min_counter == 2