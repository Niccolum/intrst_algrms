from functools import lru_cache
from collections import namedtuple
from typing import Tuple

Item = namedtuple('Item', 'name value weight')
Knapsack = namedtuple('Knapsack', 'items weight_limit')


def knapsack_standard_solution(items: Tuple[Item], weight_limit: int) -> Item:
    """https://codereview.stackexchange.com/a/20581"""

    @lru_cache(maxsize=None)
    def best_value(i: int, j: int):
        if j < 0:
            return float('-inf')
        if i == 0:
            return 0
        value, weight = items[i - 1].value, items[i - 1].weight
        res = max(best_value(i - 1, j),
                  best_value(i - 1, j - weight) + value)
        return res

    for k in reversed(range(len(items))):
        if best_value(k + 1, weight_limit) != best_value(k, weight_limit):
            yield items[k]
            weight_limit -= items[k].weight
