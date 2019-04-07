from collections import namedtuple
from itertools import permutations
import timeit

Item = namedtuple('Item', 'name value weight')
items = (
    Item('water', 10, 3),
    Item('book', 3, 1),
    Item('food', 9, 2),
    Item('jacket', 5, 2),
    Item('camera', 6, 1)
)
weight_limit = 6


def first():
    def knapsack(items, weight_limit):
        result = []

        def best_value(nitems, weight_limit):
            if nitems == 0:
                return 0
            elif items[nitems - 1].weight > weight_limit:
                return best_value(nitems - 1, weight_limit)
            else:
                value = items[nitems - 1].value
                weight = items[nitems - 1].weight
                return max(
                    best_value(nitems - 1, weight_limit),
                    best_value(nitems - 1, weight_limit - weight) + value)

        for i in reversed(range(len(items))):
            if best_value(i + 1, weight_limit) > best_value(i, weight_limit):
                result.append(items[i])
                weight_limit -= items[i].weight
        result.reverse()
        return result
    return knapsack(items, weight_limit)


def second():
    def knapsack(items, weight_limit):
        def bestvalue(i, j):
            if j < 0:
                return float('-inf')
            if i == 0:
                return 0
            value, weight = items[i - 1].value, items[i - 1].weight
            res = max(bestvalue(i - 1, j),
                      bestvalue(i - 1, j - weight) + value)
            return res

        j = weight_limit
        result = []
        for i in reversed(range(len(items))):
            if bestvalue(i + 1, j) != bestvalue(i, j):
                result.append(items[i])
                j -= items[i].weight
        result.reverse()
        return result
    return knapsack(items, weight_limit)

def third():
    def knapsack(items, weight_limit):
        n = items
        k = weight_limit
        result = []
        F = [ [0] * (k + 1) for i in range(len(n))]
        for i in range(len(n)):
            for k in range(1, k + 1):
                weight = n[i].weight
                value = n[i].value
                if k >= weight:
                    F[i][k] = max(F[i - 1][k], F[i - 1][k - weight] + value)
                else:
                    F[i][k] = F[i - 1][k]
        for i in reversed(range(len(items))):
            if F[i][k] != F[i - 1][k]:
                result.append(items[i])
                k -= n[i].weight
        result.reverse()
        return result
    return knapsack(items, weight_limit)


if __name__ == '__main__':
    print('First:\n', first(), sep='')
    print('Second:\n', second(), sep='')
    print('Third:\n', third(), sep='')
    # print('First:', timeit.timeit(
    #     stmt='first()', setup="from __main__ import first", number=100000))
    # print('Second:', timeit.timeit(
    #     stmt='second()', setup="from __main__ import second", number=100000))
    # print('Third:', timeit.timeit(
    #     stmt='third()', setup="from __main__ import third", number=100000))
    # First: 4.973978376947343
    # Second: 5.425468286965042
    # Third: 1.7679201629944146
