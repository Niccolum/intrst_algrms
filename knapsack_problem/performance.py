from collections import defaultdict
import timeit
import json
from contextlib import contextmanager
import time
from typing import List, Callable, Dict, Union
from numbers import Integral

from knapsack_problem import BASEDIR
from knapsack_problem.data import create_dynamic_knapsacks
from knapsack_problem.ref_func import Knapsack, Item
from knapsack_problem.funcs import (
    knapsack_1_standard_solution,
    knapsack_2_solution,
    knapsack_3_solution,
    knapsack_4_bruteforce_solution,
    knapsack_5_dynamic_solution,
    knapsack_6_recursive_dynamic_solution,
    knapsack_greedy_solution
)

RETRY_NUM = 1000
TOO_LONG = 60  # in seconds
SETUP_IMPORT_TEMPLATE = '''
from __main__ import {func_name} as knapsack_solution, {datalist_name} as raw_datalist
datalist = raw_datalist['{datalist_key}']
'''
RUNNING_TEMPLATE = "raw_result = knapsack_solution(*datalist['input'])"
RESULT_TO_LIST_TEMPLATE = RUNNING_TEMPLATE + '\nraw_result = list(raw_result)'
SMALL_STAT_NAME = 'small_perf'
BIG_STAT_NAME = 'big_perf'


def mean(numbers: List[Integral]) -> int:
    return sum(numbers) / len(numbers) / RETRY_NUM


@contextmanager
def time_time(msg: str) -> None:
    start = time.monotonic()
    yield start
    print('{} done: '.format(msg), time.monotonic() - start)


perf_funcs_without_bruteforce = [
    knapsack_1_standard_solution,
    knapsack_2_solution,
    knapsack_3_solution,
    knapsack_5_dynamic_solution,
    knapsack_6_recursive_dynamic_solution,
    knapsack_greedy_solution
]
perf_funcs_with_bruteforce = perf_funcs_without_bruteforce[:] + [knapsack_4_bruteforce_solution]

result = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))


def small_perf() -> None:
    common_perf_part(funcs=perf_funcs_with_bruteforce, datalists=perf_small_datalists, stat_name=SMALL_STAT_NAME)


def big_perf() -> None:
    common_perf_part(funcs=perf_funcs_without_bruteforce, datalists=perf_datalists, stat_name=BIG_STAT_NAME)


def common_perf_part(*,
                     funcs: List[Callable],
                     datalists: Dict[str, Dict[str, Union[Knapsack, List[Item]]]],
                     stat_name: str) -> None:
    datalists_name = next(k for k, v in globals().items() if v == datalists)
    for func in funcs:
        func_name = func.__name__
        print('\n' + '*' * 10, func_name, '*' * 10)
        for datalist_name, _ in list(datalists.items()):
            print('\n' + datalist_name)

            with time_time(stat_name) as start_time:
                result[stat_name][func_name][datalist_name] = mean(
                    timeit.repeat(
                        RESULT_TO_LIST_TEMPLATE,
                        setup=SETUP_IMPORT_TEMPLATE.format(
                            func_name=func_name,
                            datalist_name=datalists_name,
                            datalist_key=datalist_name),
                        number=RETRY_NUM
                    )
                )
            if time.monotonic() - start_time > TOO_LONG:
                break


def main() -> None:
    small_perf()
    big_perf()
    with open(BASEDIR / 'performance.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)
        print('Done')


if __name__ == '__main__':
    perf_small_datalists = create_dynamic_knapsacks(start=3, end=30, step=3)
    perf_datalists = create_dynamic_knapsacks(start=30, end=450, step=30)
    main()
