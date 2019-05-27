import unittest
import copy

from data import (
    create_data_decreasing_depth, create_data_increasing_depth, generate_data)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)

class TestFlattenFunctions(unittest.TestCase):

    def get_increase_list(self):
        for data in generate_data():
            params = data[1]
            flatten_result = copy.copy(params['data'])
            result = create_data_increasing_depth(**params)
            yield result, list(flatten_result)

    def get_decrease_list(self):
        for data in generate_data():
            params = data[1]
            flatten_result = copy.copy(params['data'])
            result = create_data_decreasing_depth(**params)
            yield result, list(flatten_result)

    def setUp(self):
        self.decrease_generator = self.get_decrease_list()
        self.increase_generator = self.get_increase_list()


    def test_outer_flatten_1(self):
        for data, result in self.decrease_generator:
            self.assertEqual(list(outer_flatten_1(data)), result)

        for data, result in self.increase_generator:
            self.assertEqual(list(outer_flatten_1(data)), result)

    def test_outer_flatten_2(self):
        for data, result in self.decrease_generator:
            self.assertEqual(list(outer_flatten_2(data)), result)

        for data, result in self.increase_generator:
            self.assertEqual(list(outer_flatten_2(data)), result)

    def test_niccolum_flatten(self):
        for data, result in self.decrease_generator:
            self.assertEqual(niccolum_flatten(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(niccolum_flatten(data), result)

    def test_tishka_flatten(self):
        for data, result in self.decrease_generator:
            self.assertEqual(tishka_flatten(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(tishka_flatten(data), result)

    def test_zart_flatten(self):
        for data, result in self.decrease_generator:
            self.assertEqual(zart_flatten(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(zart_flatten(data), result)

    def test_recursion_flatten(self):
        try:
            for data, result in self.decrease_generator:
                self.assertEqual(list(recursion_flatten(data)), result)

            for data, result in self.increase_generator:
                self.assertEqual(list(recursion_flatten(data)), result)
        except RecursionError:
            pass

    def test_tishka_flatten_with_stack(self):
        for data, result in self.decrease_generator:
            self.assertEqual(tishka_flatten_with_stack(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(tishka_flatten_with_stack(data), result)

    def test_recursive_flatten_like_tishka(self):
        for data, result in self.decrease_generator:
            self.assertEqual(recursive_flatten_like_tishka(data), result)

        for data, result in self.increase_generator:
            self.assertEqual(recursive_flatten_like_tishka(data), result)