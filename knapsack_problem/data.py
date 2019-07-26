from collections import namedtuple

Item = namedtuple('Item', 'name value weight')
Knapsack = namedtuple('Knapsack', 'items weight')


def pack_up_knapsack_1():
    """
    expected result
    [
        Item(name='water', value=10, weight=3),
        Item(name='food', value=9, weight=2),
        Item(name='camera', value=6, weight=1)
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


def pack_up_knapsack_2():
    """
    expected result
    (
    11,
    [
        Item(name='water', value=6, weight=4),
        Item(name='food', value=2, weight=1),
        Item(name='camera', value=4, weight=12),
        Item(name='book', value=1, weight=1)
    ]
    )
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


knapsack_1 = pack_up_knapsack_1()
knapsack_2 = pack_up_knapsack_2()