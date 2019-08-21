import unittest

from data import (
    create_data_decreasing_depth, create_data_increasing_depth)


class TestGenerationData(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [
            {
                'data': iter(range(10)),
                'max_depth': 3,
                'length': 2,
                'result': {
                    'increase': [0, 1, [2, 3, [4, 5]], 6, 7, [8, 9]],
                    'decrease': [[[0, 1], 2, 3], 4, 5, [[6, 7], 8, 9]],
                },
            }, {
                'data': iter(range(10)),
                'max_depth': 8,
                'length': 1,
                'result': {
                    'increase': [0, [1, [2, [3, [4, [5, [6, [7]]]]]]], 8, [9]],
                    'decrease': [[[[[[[[0], 1], 2], 3], 4], 5], 6], 7,
                                 [[[[[[[8], 9]]]]]]],
                },
            }, {
                'data': iter(range(10)),
                'max_depth': 1,
                'length': 1,
                'result': {
                    'increase': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    'decrease': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                },
            }, {
                'data': iter(range(10)),
                'max_depth': 10,
                'length': 10,
                'result': {
                    'increase': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    'decrease': [[[[[[[[[[
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                    ]]]]]]]]]],
                },
            },
        ]

    def test_create_data_decreasing_depth(self) -> None:
        for data in self.test_data:
            params = {k: v for k, v in data.items() if k != 'result'}
            result = create_data_decreasing_depth(**params)
            self.assertEqual(result, data['result']['decrease'])

    def test_create_data_increasing_depth(self) -> None:
        for data in self.test_data:
            params = {k: v for k, v in data.items() if k != 'result'}
            result = create_data_increasing_depth(**params)
            self.assertEqual(result, data['result']['increase'])
