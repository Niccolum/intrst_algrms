import random
from typing import Dict, List, Union

from random_word import RandomWords

from ref_func import knapsack_standard_solution as knapsack_func, Item, Knapsack


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


def create_dynamic_knapsacks() -> Dict[str, Dict[str, Union[Knapsack, List[Item]]]]:
    knapsacks = dict()
    for i in range(1, 6):
        weight_limit = 10 ** i
        knapsack_key = 'knapsack_{weight_limit}'.format(weight_limit=weight_limit)
        knapsacks[knapsack_key] = dict()

        knapsack_question = create_knapsack(weight_limit)
        knapsack_answer = knapsack_func(*knapsack_question)

        knapsacks[knapsack_key]['question'] = knapsack_question
        knapsacks[knapsack_key]['answer'] = knapsack_answer

    return knapsacks


def create_knapsack(weight_limit: int) -> Knapsack:
    r = RandomWords()
    words = r.get_random_words(limit=weight_limit)

    items = []
    for i in range(weight_limit):
        word = words[i]
        value = random.randrange(1, 100)
        weight = random.randrange(1, 100)
        item = Item(word, value, weight)
        items.append(item)

    return Knapsack(items, weight_limit)