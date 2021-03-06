import unittest
import copy
import time
from typing import List, Union, Iterator

from unpacking_flatten_lists.data import (
    create_data_decreasing_depth,
    create_data_increasing_depth,
    generate_data)
from unpacking_flatten_lists.funcs import (
    outer_flatten_1,
    outer_flatten_2,
    niccolum_flatten,
    tishka_flatten,
    zart_flatten,
    recursive_flatten_iterator,
    tishka_flatten_with_stack,
    recursive_flatten_generator,
    profile)

Num = Union[int, float]


class TestFlattenFunctions(unittest.TestCase):

    @staticmethod
    def get_increase_list() -> Union[List, Iterator]:
        for data in generate_data():
            params = data[1]
            flatten_result = copy.copy(params['data'])
            result = create_data_increasing_depth(**params)
            yield result, list(flatten_result)

    @staticmethod
    def get_decrease_list() -> Union[List, Iterator]:
        for data in generate_data():
            params = data[1]
            flatten_result = copy.copy(params['data'])
            result = create_data_decreasing_depth(**params)
            yield result, list(flatten_result)

    def setUp(self) -> None:
        self.decrease_generator = self.get_decrease_list()
        self.increase_generator = self.get_increase_list()
        self._started_at = time.time()

    def tearDown(self) -> None:
        elapsed = time.time() - self._started_at
        print('{}s'.format(round(elapsed, 5)))

    def test_outer_flatten_1(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(list(outer_flatten_1(data)), result)

        for data, result in self.increase_generator:
            self.assertEqual(list(outer_flatten_1(data)), result)

    def test_outer_flatten_2(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(list(outer_flatten_2(data)), result)

        for data, result in self.increase_generator:
            self.assertEqual(list(outer_flatten_2(data)), result)

    def test_niccolum_flatten(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(niccolum_flatten(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(niccolum_flatten(data), result)

    def test_tishka_flatten(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(tishka_flatten(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(tishka_flatten(data), result)

    def test_zart_flatten(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(zart_flatten(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(zart_flatten(data), result)

    def test_recursive_flatten_iterator(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(list(recursive_flatten_iterator(data)), result)

        for data, result in self.increase_generator:
            self.assertEqual(list(recursive_flatten_iterator(data)), result)

    def test_tishka_flatten_with_stack(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(tishka_flatten_with_stack(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(tishka_flatten_with_stack(data), result)

    def test_recursive_flatten_generator(self) -> None:
        for data, result in self.decrease_generator:
            self.assertEqual(recursive_flatten_generator(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(recursive_flatten_generator(data), result)


class TestProfileFlattenFunctions(unittest.TestCase):

    def test_profile(self) -> None:
        # funcs done correctly
        self.assertEqual(profile(), None)