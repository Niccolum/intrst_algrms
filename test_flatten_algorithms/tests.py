import unittest

from data import (
    create_data_decreasing_depth, create_data_increasing_depth, generate_data)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)

# tests data generators


class TestGenerationData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_data = [
            {
                'data': list(range(10)),
                'max_depth': 3
                'length': 2
                'result': {
                    'increase': [0, 1, [2, 3, [4, 5]], 6, 7, [8, 9]],
                    'decrease': [[[0, 1], 2, 3], 4, 5, [[6, 7], 8, 9]],
                }
            }, {
                'data': list(range(10)),
                'max_depth': 8
                'length': 1
                'result': {
                    'increase': [0, [1, [2, [3, [4, [5, [6, [7]]]]]]], 8, [9]],
                    'decrease': [[[[[[[[0], 1], 2], 3], 4], 5], 6], 7,
                                 [[[[[[[8, 9]]]]]]]],
                }
            }, {
                'data': list(range(10)),
                'max_depth': 1
                'length': 1
                'result': {
                    'increase': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    'decrease': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                }
            }, {
                'data': list(range(10)),
                'max_depth': 10
                'length': 10
                'result': {
                    'increase': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    'decrease': [[[[[[[[[[
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                    ]]]]]]]]]],
                }
            },
        ]

    def test_create_data_decreasing_depth(self):
        for data in self.test_data:
            params = {k: v for k, v in data.items() if k != 'result'}
            result = create_data_decreasing_depth(**params)
            self.assertEqual(result, data['result']['decrease'])

    def test_create_data_increasing_depth(self):
        for data in self.test_data:
            params = {k: v for k, v in data.items() if k != 'result'}
            result = create_data_decreasing_depth(**params)
            self.assertEqual(result, data['result']['increase'])


class TestGenerationData(unittest.TestCase):

    def get_increase_list(self):
        for data in generate_data():
            params = data[1]
            yield create_data_increasing_depth(params), params['data']

    def get_decrease_list(self):
        for data in generate_data():
            params = data[1]
            yield create_data_decreasing_depth(params), params['data']

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
        for data, result in self.decrease_generator:
            self.assertEqual(list(recursion_flatten(data)), result)

        for data, result in self.increase_generator:
            self.assertEqual(list(recursion_flatten(data)), result)

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