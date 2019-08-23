"""
Abstract helper module for check correct other solutions in tests
Also define "Item" and "Knapsack" abstract types
"""
import sys
from functools import lru_cache
from collections import namedtuple
from typing import Tuple

sys.setrecursionlimit(10_000)


class Item(namedtuple('Item', 'name value weight')):
    """
    Atomic thing with his own characteristics

    .. py:attribute:: name:

        Name of item

    .. py:attribute:: value:

        Cost of item

    .. py:attribute:: weight:

        Weight of item
    """


class Knapsack(namedtuple('Knapsack', 'items weight_limit')):
    """
    Knapsack characteristics

    .. py:attribute:: items:

        one of Item above

    .. py:attribute:: weight_limit:

        limit of Knapsack for items
    """


def knapsack_standard_solution(items: Tuple[Item], weight_limit: int) -> Item:
    """
    Standard solution for knapsack problem in Python
    https://codereview.stackexchange.com/a/20581
    """

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
