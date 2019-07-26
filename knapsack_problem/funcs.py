"""
Examples of python realization of knapsack problem

Some Theory:
The knapsack problem or rucksack problem is a problem in combinatorial optimization:
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so
that the total weight is less than or equal to a given limit and the total value is as large as possible.
It derives its name from the problem faced by someone
who is constrained by a fixed-size knapsack and must fill it with the most valuable items.
(https://en.wikipedia.org/wiki/Knapsack_problem)
"""
from functools import lru_cache


def knapsack_first(items, weight_limit):
    """
    https://codereview.stackexchange.com/a/20581

    Solve the knapsack problem by finding the most valuable subsequence
    of items that weighs no more than weight_limit.

    items must be a sequence of pairs (value, weight), where value is a
    number and weight is a non-negative integer.

    weight_limit is a non-negative integer.

    Return a pair whose first element is the sum of values in the most
    valuable subsequence, and whose second element is the subsequence.
    """

    @lru_cache(maxsize=None)
    def best_value(i, j):
        if j < 0:
            return float('-inf')
        if i == 0:
            return 0
        value, weight = items[i - 1].value, items[i - 1].weight
        res = max(best_value(i - 1, j),
                  best_value(i - 1, j - weight) + value)
        return res

    max_weight = weight_limit
    result = []
    for k in reversed(range(len(items))):
        if best_value(k + 1, weight_limit) != best_value(k, weight_limit):
            result.append(items[k])
            weight_limit -= items[k].weight
    result.reverse()
    return best_value(len(items), max_weight), result


def knapsack_second(items, weight_limit):
    n = items
    k = weight_limit
    result = []
    f = [[0] * (k + 1) for i in range(len(n))]
    for i in range(len(n)):
        for k in range(1, k + 1):
            weight = n[i].weight
            value = n[i].value
            if k >= weight:
                f[i][k] = max(f[i - 1][k], f[i - 1][k - weight] + value)
            else:
                f[i][k] = f[i - 1][k]

    for i in reversed(range(len(items))):
        if f[i][k] != f[i - 1][k]:
            result.append(items[i])
            k -= n[i].weight
    result.reverse()
    return result

#https://www.sanfoundry.com/python-program-solve-0-1-knapsack-problem-using-dynamic-programming-memoization/
#https://codereview.stackexchange.com/a/125386
#https://codereview.stackexchange.com/a/62871
#https://codereview.stackexchange.com/a/220499
#https://codereview.stackexchange.com/a/162179
#http://rosettacode.org/wiki/Knapsack_problem/0-1#Python
if __name__ == '__main__':
    from data import knapsack_1
    print(knapsack_first(*knapsack_1))
