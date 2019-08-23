import random
import math
import itertools
from collections import OrderedDict
import urllib.request
from typing import Dict, Union, Tuple

from knapsack_problem.ref_func import knapsack_standard_solution as knapsack_func, Item, Knapsack

"""
functions with "_static_" in name - correct proven examples of input output for knapsack problem
So, for debugging funcs.py I used it for checking correct behavior, because
output of "_static_" functions write in docstrings and we can compare strings with construction:

.. code:: python

    from operator import attrgetter
    expected_result = data.__doc__.replace('\n', '').replace(' ', '')
    result = sorted(func(*data()), key=attrgetter('name'))
    result = str(result).replace(' ', '')

For all other tests i use random data with as many arguments as I need
For output I use one of funcs, reference function, on which correct I am convinced
It's on ref_func.py
But i still use it for other test for check other parameters, not only correctness
"""


def pack_up_static_knapsack_1() -> Knapsack:
    """
    [

        Item(name='camera', value=6, weight=1),
        Item(name='food', value=9, weight=2),
        Item(name='water', value=10, weight=3)

    ]
    """
    items = (
        Item('water', 10, 3),
        Item('book', 3, 1),
        Item('food', 9, 2),
        Item('jacket', 5, 2),
        Item('camera', 6, 1)
    )
    weight_limit = 6

    return Knapsack(items, weight_limit)


def pack_up_static_knapsack_2() -> Knapsack:
    """
    [

        Item(name='book', value=1, weight=1),
        Item(name='food', value=2, weight=1),
        Item(name='jacket', value=2, weight=2),
        Item(name='water', value=6, weight=4)

    ]
    """
    items = (
        Item('water', 6, 4),
        Item('book', 1, 1),
        Item('food', 2, 1),
        Item('jacket', 2, 2),
        Item('camera', 4, 12)
    )
    weight_limit = 15

    return Knapsack(items, weight_limit)


def pack_up_static_knapsack_3() -> Knapsack:
    """
    [

        Item(name='apple', value=39, weight=40),
        Item(name='beer', value=52, weight=10),
        Item(name='book', value=30, weight=10),
        Item(name='camera', value=32, weight=30),
        Item(name='t-shirt', value=24, weight=15),
        Item(name='tin', value=68, weight=45),
        Item(name='trousers', value=48, weight=10),
        Item(name='umbrella', value=73, weight=40),
        Item(name='water', value=153, weight=200)

    ]
    """
    items = (
        Item("map", 9, 150),
        Item("compass", 13, 35),
        Item("water", 153, 200),
        Item("sandwich", 50, 160),
        Item("glucose", 15, 60),
        Item("tin", 68, 45),
        Item("banana", 27, 60),
        Item("apple", 39, 40),
        Item("cheese", 23, 30),
        Item("beer", 52, 10),
        Item("suntan cream", 11, 70),
        Item("camera", 32, 30),
        Item("t-shirt", 24, 15),
        Item("trousers", 48, 10),
        Item("umbrella", 73, 40),
        Item("waterproof trousers", 42, 70),
        Item("waterproof overclothes", 43, 75),
        Item("note-case", 22, 80),
        Item("sunglasses", 7, 20),
        Item("towel", 18, 12),
        Item("socks", 4, 50),
        Item("book", 30, 10)
    )
    weight_limit = 400

    return Knapsack(items, weight_limit)


def create_dynamic_knapsacks(*, start: int, end: int, step: int = 1) -> \
        Dict[str, Dict[str, Union[Knapsack, Tuple[Item]]]]:
    """
    Dynamic create collections of Items
    as result -> {

        knapsack_*weight_limit*: {

            'input':  Tuple[Item] # generated items
            'output': Knapsack # Knapsack answer by knapsack_standard_solution (for checking with other solutions)

    }
    """

    knapsacks = OrderedDict()
    for i in range(start, end + 1, step):
        weight_limit = i
        knapsack_key = 'knapsack_{weight_limit}'.format(weight_limit=weight_limit)
        knapsacks.setdefault(knapsack_key, dict())

        knapsack_question = _create_knapsack(weight_limit)
        knapsack_answer = tuple(knapsack_func(*knapsack_question))

        knapsacks[knapsack_key]['input'] = knapsack_question
        knapsacks[knapsack_key]['output'] = knapsack_answer

    return knapsacks


def _create_knapsack(weight_limit: int) -> Knapsack:
    words = _get_random_words(limit=weight_limit)

    # create list of unique tuples for smallest spread for items value and weight, depends on weight_limit
    max_spread = math.ceil(math.sqrt(weight_limit) * 2)
    values_items_list = list(itertools.product(range(1, max_spread), repeat=2))
    random.shuffle(values_items_list)

    items = []
    for word in words:
        value, weight = values_items_list.pop()
        item = Item(word, value, weight)
        items.append(item)

    return Knapsack(tuple(items), weight_limit)


def _get_random_words(limit=None):
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()[:limit]
    random.shuffle(words)
    while words:
        yield words.pop()
