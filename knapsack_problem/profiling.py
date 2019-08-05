from typing import Callable, Union, List

from memprof import memprof

from funcs import (
    knapsack_1_standard_solution,
    knapsack_2_solution,
    knapsack_3_solution,
    knapsack_4_bruteforce_solution,
    knapsack_5_dynamic_solution,
    knapsack_6_recursive_dynamic_solution,
    knapsack_greedy_solution
)
from data import create_dynamic_knapsacks
from ref_func import Item


def abstract_wrapper(*, func: Callable, start: int) -> Union[Item, List[Item], List[None]]:
    data = create_dynamic_knapsacks(start=start, end=start + 1)
    data = list(data.values())[0]
    input_data = data['input']
    del data
    return func(*input_data)


@memprof(threshold=1024, plot=True)
def datalist_10_knapsack_1_solution() -> list:
    func = knapsack_1_standard_solution
    start = 10
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_25_knapsack_1_solution() -> list:
    func = knapsack_1_standard_solution
    start = 25
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_100_knapsack_1_solution() -> list:
    func = knapsack_1_standard_solution
    start = 100
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_500_knapsack_1_solution() -> list:
    func = knapsack_1_standard_solution
    start = 500
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_1_000_knapsack_1_solution() -> list:
    func = knapsack_1_standard_solution
    start = 1_000
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_2_000_knapsack_1_solution() -> list:
    func = knapsack_1_standard_solution
    start = 2_000
    return list(abstract_wrapper(func=func, start=start))


datalist_10_knapsack_1_solution()
datalist_25_knapsack_1_solution()
datalist_100_knapsack_1_solution()
datalist_500_knapsack_1_solution()
datalist_1_000_knapsack_1_solution()
datalist_2_000_knapsack_1_solution()

#  ******************************************************


@memprof(threshold=1024, plot=True)
def datalist_10_knapsack_2_solution() -> list:
    func = knapsack_2_solution
    start = 10
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_25_knapsack_2_solution() -> list:
    func = knapsack_2_solution
    start = 25
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_100_knapsack_2_solution() -> list:
    func = knapsack_2_solution
    start = 100
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_500_knapsack_2_solution() -> list:
    func = knapsack_2_solution
    start = 500
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_1_000_knapsack_2_solution() -> list:
    func = knapsack_2_solution
    start = 1_000
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_2_000_knapsack_2_solution() -> list:
    func = knapsack_2_solution
    start = 2_000
    return list(abstract_wrapper(func=func, start=start))


datalist_10_knapsack_2_solution()
datalist_25_knapsack_2_solution()
datalist_100_knapsack_2_solution()
datalist_500_knapsack_2_solution()
datalist_1_000_knapsack_2_solution()
datalist_2_000_knapsack_2_solution()

#  ******************************************************


@memprof(threshold=1024, plot=True)
def datalist_10_knapsack_3_solution() -> list:
    func = knapsack_3_solution
    start = 10
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_25_knapsack_3_solution() -> list:
    func = knapsack_3_solution
    start = 25
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_100_knapsack_3_solution() -> list:
    func = knapsack_3_solution
    start = 100
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_500_knapsack_3_solution() -> list:
    func = knapsack_3_solution
    start = 500
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_1_000_knapsack_3_solution() -> list:
    func = knapsack_3_solution
    start = 1_000
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_2_000_knapsack_3_solution() -> list:
    func = knapsack_3_solution
    start = 2_000
    return list(abstract_wrapper(func=func, start=start))


datalist_10_knapsack_3_solution()
datalist_25_knapsack_3_solution()
datalist_100_knapsack_3_solution()
datalist_500_knapsack_3_solution()
datalist_1_000_knapsack_3_solution()
datalist_2_000_knapsack_3_solution()

#  ******************************************************


@memprof(threshold=1024, plot=True)
def datalist_10_knapsack_4_solution() -> list:
    func = knapsack_4_bruteforce_solution
    start = 10
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_25_knapsack_4_solution() -> list:
    func = knapsack_4_bruteforce_solution
    start = 25
    return list(abstract_wrapper(func=func, start=start))


datalist_10_knapsack_4_solution()
datalist_25_knapsack_4_solution()

#  ******************************************************


@memprof(threshold=1024, plot=True)
def datalist_10_knapsack_5_solution() -> list:
    func = knapsack_5_dynamic_solution
    start = 10
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_25_knapsack_5_solution() -> list:
    func = knapsack_5_dynamic_solution
    start = 25
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_100_knapsack_5_solution() -> list:
    func = knapsack_5_dynamic_solution
    start = 100
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_500_knapsack_5_solution() -> list:
    func = knapsack_5_dynamic_solution
    start = 500
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_1_000_knapsack_5_solution() -> list:
    func = knapsack_5_dynamic_solution
    start = 1_000
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_2_000_knapsack_5_solution() -> list:
    func = knapsack_5_dynamic_solution
    start = 2_000
    return list(abstract_wrapper(func=func, start=start))


datalist_10_knapsack_5_solution()
datalist_25_knapsack_5_solution()
datalist_100_knapsack_5_solution()
datalist_500_knapsack_5_solution()
datalist_1_000_knapsack_5_solution()
datalist_2_000_knapsack_5_solution()

#  ******************************************************


@memprof(threshold=1024, plot=True)
def datalist_10_knapsack_6_solution() -> list:
    func = knapsack_6_recursive_dynamic_solution
    start = 10
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_25_knapsack_6_solution() -> list:
    func = knapsack_6_recursive_dynamic_solution
    start = 25
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_100_knapsack_6_solution() -> list:
    func = knapsack_6_recursive_dynamic_solution
    start = 100
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_500_knapsack_6_solution() -> list:
    func = knapsack_6_recursive_dynamic_solution
    start = 500
    return list(abstract_wrapper(func=func, start=start))


datalist_10_knapsack_6_solution()
datalist_25_knapsack_6_solution()
datalist_100_knapsack_6_solution()
datalist_500_knapsack_6_solution()

#  ******************************************************


@memprof(threshold=1024, plot=True)
def datalist_10_knapsack_greedy_solution() -> list:
    func = knapsack_greedy_solution
    start = 10
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_25_knapsack_greedy_solution() -> list:
    func = knapsack_greedy_solution
    start = 25
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_100_knapsack_greedy_solution() -> list:
    func = knapsack_greedy_solution
    start = 100
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_500_knapsack_greedy_solution() -> list:
    func = knapsack_greedy_solution
    start = 500
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_1_000_knapsack_greedy_solution() -> list:
    func = knapsack_6_recursive_dynamic_solution
    start = 1_000
    return list(abstract_wrapper(func=func, start=start))


@memprof(threshold=1024, plot=True)
def datalist_2_000_knapsack_greedy_solution() -> list:
    func = knapsack_6_recursive_dynamic_solution
    start = 2_000
    return list(abstract_wrapper(func=func, start=start))


datalist_10_knapsack_greedy_solution()
datalist_25_knapsack_greedy_solution()
datalist_100_knapsack_greedy_solution()
datalist_500_knapsack_greedy_solution()
datalist_1_000_knapsack_greedy_solution()
datalist_2_000_knapsack_greedy_solution()
