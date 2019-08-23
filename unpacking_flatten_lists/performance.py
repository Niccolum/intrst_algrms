import timeit
import json
import time
from collections import defaultdict
from typing import List, Callable
from numbers import Integral
from contextlib import contextmanager

from unpacking_flatten_lists import BASEDIR
from unpacking_flatten_lists.data import (
    generate_data,
    create_data_decreasing_depth,
    create_data_increasing_depth)
from unpacking_flatten_lists.funcs import (
    outer_flatten_1,
    outer_flatten_2,
    niccolum_flatten,
    tishka_flatten,
    zart_flatten,
    recursion_flatten,
    tishka_flatten_with_stack,
    recursive_flatten_like_tishka)

RETRY_NUM = 10
TOO_LONG = 60 * 5 // 100  # in seconds
INCREMENT_MODE_NAME = 'increase'
DECREMENT_MODE_NAME = 'decrease'
SETUP_IMPORT_TEMPLATE = '''
from typing import Generator
import json
from __main__ import {func_name} as flatten
data = json.loads("{data}")
'''
RUNNING_TEMPLATE = '''
result = flatten(data)
if isinstance(result, Generator):
    result = list(result)
'''


funcs = [
    outer_flatten_1,
    outer_flatten_2,
    niccolum_flatten,
    tishka_flatten,
    zart_flatten,
    recursion_flatten,
    tishka_flatten_with_stack,
    recursive_flatten_like_tishka
]

result = defaultdict(lambda: defaultdict(lambda: defaultdict(Integral)))


def mean(numbers: List[Integral]) -> int:
    return sum(numbers) / len(numbers) / RETRY_NUM


@contextmanager
def time_time(msg: str) -> None:
    start = time.monotonic()
    yield start
    print('{} done: '.format(msg), time.monotonic() - start)


def increase_part():
    print('*' * 10, 'Increase', '*' * 10)
    common_part(data_create_func=create_data_increasing_depth, mode=INCREMENT_MODE_NAME)


def decrease_part():
    print('*' * 10, 'Decrease', '*' * 10)
    common_part(data_create_func=create_data_decreasing_depth, mode=DECREMENT_MODE_NAME)


def common_part(*, data_create_func: Callable, mode: str):
    for func in funcs:
        func_name = func.__name__

        print('\n', func_name, '\n')

        for data_example in generate_data():
            data = data_create_func(**data_example[1])
            data = json.dumps(data)  # crutch because timeit has s_push: parser stack overflow for list with 100 deep
            data_struct_name = data_example[0]

            with time_time(data_struct_name) as start_time:
                result[func_name][mode][data_struct_name] = mean(
                    timeit.repeat(
                        RUNNING_TEMPLATE,
                        setup=SETUP_IMPORT_TEMPLATE.format(
                            func_name=func_name,
                            data=data),
                        number=RETRY_NUM
                    )
                )
            if time.monotonic() - start_time > TOO_LONG:
                break


def main():
    increase_part()
    decrease_part()

    print('Done testing. Writes...')
    with open(BASEDIR / 'performance.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)
        print('Done')


if __name__ == '__main__':
    main()