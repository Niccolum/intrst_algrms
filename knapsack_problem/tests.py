import unittest
from operator import attrgetter
from typing import Callable
import time

from knapsack_problem.data import (
    pack_up_static_knapsack_1,
    pack_up_static_knapsack_2,
    pack_up_static_knapsack_3,
    create_dynamic_knapsacks
)
from knapsack_problem.funcs import (
    knapsack_1_standard_solution,
    knapsack_2_solution,
    knapsack_3_solution,
    knapsack_4_bruteforce_solution,
    knapsack_5_dynamic_solution,
    knapsack_6_recursive_dynamic_solution,
    knapsack_greedy_solution
)
from knapsack_problem.ref_func import knapsack_standard_solution

TOO_LONG = 60 * 1  # time in seconds for break loop of testing functions


class TestKnapsackProblem1StaticData(unittest.TestCase):
    dataset = [pack_up_static_knapsack_1, pack_up_static_knapsack_2, pack_up_static_knapsack_3]

    @classmethod
    def setUpClass(cls) -> None:
        print('*' * 15, cls.__name__, '*' * 15)

    def main_part(self, *, func: Callable) -> None:
        print('#' * 5, func.__name__, '#' * 5)
        for data in self.dataset:
            expected_result = data.__doc__.replace('\n', '').replace(' ', '')

            start = time.monotonic()
            result = sorted(func(*data()), key=attrgetter('name'))
            result = str(result).replace(' ', '')
            end = time.monotonic() - start
            self.assertEqual(expected_result, result)
            print('Knapsack with {} items was completed in {:2f} seconds'.format(len(data().items), end))

    def test_knapsack_1_solution(self) -> None:
        self.main_part(func=knapsack_1_standard_solution)

    def test_knapsack_2_solution(self) -> None:
        self.main_part(func=knapsack_2_solution)

    def test_knapsack_3_solution(self) -> None:
        self.main_part(func=knapsack_3_solution)

    def test_knapsack_4_solution(self) -> None:
        self.main_part(func=knapsack_4_bruteforce_solution)

    def test_knapsack_5_solution(self) -> None:
        self.main_part(func=knapsack_5_dynamic_solution)

    def test_knapsack_6_solution(self) -> None:
        self.main_part(func=knapsack_6_recursive_dynamic_solution)

    def test_knapsack_greedy_solution(self) -> None:
        print('#' * 5, knapsack_greedy_solution.__name__, '#' * 5)
        for data in self.dataset:
            knapsack = data()

            start = time.monotonic()
            raw_result = list(knapsack_greedy_solution(*knapsack))
            self.assertTrue(knapsack.weight_limit >= sum(i.weight for i in raw_result))
            end = time.monotonic() - start

            raw_expected_result = knapsack_standard_solution(*knapsack)
            expected_result = sum(i.value for i in raw_expected_result) * 0.9
            result = sum(i.value for i in raw_result)

            self.assertTrue(result >= expected_result)
            print('Knapsack with {} items was completed in {:2f} seconds'.format(len(data().items), end))


class TestKnapsackProblem2DynamicData(unittest.TestCase):
    dataset = create_dynamic_knapsacks(start=10, end=50, step=4)

    @classmethod
    def setUpClass(cls) -> None:
        print('*' * 15, cls.__name__, '*' * 15)

    def main_part(self, func: Callable) -> None:
        print('#' * 5, func.__name__, '#' * 5)
        for data in self.dataset.values():
            expected_result = sum(i.value for i in data['output'])

            start = time.monotonic()
            raw_result = func(*data['input'])
            result = sum(i.value for i in raw_result)
            end = time.monotonic() - start

            self.assertTrue(data['input'].weight_limit >= sum(i.weight for i in raw_result))
            self.assertEqual(result, expected_result)

            print('Knapsack with {} items was completed in {:2f} seconds'.format(len(data['input'].items), end))
            if end > TOO_LONG:
                print('Function {func_name} working too long'.format(func_name=func.__name__))
                break

    def test_knapsack_1_solution(self) -> None:
        self.main_part(func=knapsack_1_standard_solution)

    def test_knapsack_2_solution(self) -> None:
        self.main_part(func=knapsack_2_solution)

    def test_knapsack_3_solution(self) -> None:
        self.main_part(func=knapsack_3_solution)

    def test_knapsack_4_solution(self) -> None:
        self.main_part(func=knapsack_4_bruteforce_solution)

    def test_knapsack_5_solution(self) -> None:
        self.main_part(func=knapsack_5_dynamic_solution)

    def test_knapsack_6_solution(self) -> None:
        self.main_part(func=knapsack_6_recursive_dynamic_solution)

    def test_knapsack_greedy_solution(self) -> None:
        print('#' * 5, knapsack_greedy_solution.__name__, '#' * 5)
        for data in self.dataset.values():
            start = time.monotonic()
            raw_result = list(knapsack_greedy_solution(*data['input']))
            end = time.monotonic() - start

            self.assertTrue(data['input'].weight_limit >= sum(i.weight for i in raw_result))

            result = sum(i.value for i in raw_result)
            expected_result = sum(i.value for i in data['output']) * 0.9
            self.assertTrue(result >= expected_result)

            print('Knapsack with {} items was completed in {:2f} seconds'.format(len(data['input'].items), end))


if __name__ == '__main__':
    unittest.main()
