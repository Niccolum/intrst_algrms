"""
Examples of python realization of solution for knapsack problem
"""
from itertools import combinations
from typing import Tuple, List, Generator, Any, Union, Iterator

from knapsack_problem.ref_func import knapsack_standard_solution, Item


# @profile
def knapsack_1_standard_solution(items: Tuple[Item], weight_limit: int) -> Item:
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
    return knapsack_standard_solution(items, weight_limit)


# @profile
def knapsack_2_solution(items: Tuple[Item], weight_limit: int) -> Item:
    """
    my own function, written thanks to the site:
    https://foxford.ru/wiki/informatika/algoritm-ukladki-ryukzaka
    """
    w = weight_limit
    f = [[0] * (w + 1) for i in range(len(items) + 1)]
    for i in range(len(items)):
        weight = items[i].weight
        value = items[i].value
        for j in range(1, w + 1):
            if j >= weight:
                f[i][j] = max(f[i - 1][j], f[i - 1][j - weight] + value)
            else:
                f[i][j] = f[i - 1][j]

    for k in reversed(range(len(items))):
        if f[k][w] != f[k - 1][w]:
            yield items[k]
            w -= items[k].weight


# @profile
def knapsack_3_solution(items: Tuple[Item], weight_limit: int) -> Item:
    """
    Given a list of items with name, value and weight.
    Return the optimal value with total weight <= allowed weight and
    list of picked items.
    https://codereview.stackexchange.com/a/125386
    """

    # find which item are picked
    def fetch_items(k: List[List[int]], weight_limit: int, items: Tuple[Item]):
        for item, weights_p, weights_n in zip(items[::-1], k[-2::-1], k[::-1]):
            if weights_n[weight_limit] != weights_p[weight_limit]:
                yield item
                weight_limit -= item.weight

    k = [
        [0] * (weight_limit + 1)
        for x in range(len(items) + 1)
    ]
    for next_idx, (item, weights) in enumerate(zip(items, k), 1):
        for w, current_weight in enumerate(weights[1:], 1):
            if item.weight <= w:
                k[next_idx][w] = max(
                    item.value + weights[w - item.weight],
                    current_weight
                )
            else:
                k[next_idx][w] = current_weight

    return fetch_items(k, weight_limit, items)


# @profile
def knapsack_4_bruteforce_solution(items: Tuple[Item], weight_limit: int) -> Union[Item, List[None]]:
    """
    Brute force algorithm
    http://rosettacode.org/mw/index.php?title=Knapsack_problem/0-1&action=edit&section=62
    """

    def any_comb(items: Tuple[Item]) -> Generator:
        """return combinations of any length from the items"""
        return (comb
                for r in range(1, len(items) + 1)
                for comb in combinations(items, r)
                )

    def total_value(comb: Tuple[Any]) -> Tuple[int, int]:
        """Totalise a particular combination of items"""
        totwt = totval = 0
        for item, val, wt in comb:
            totwt += wt
            totval += val
        return (totval, -totwt) if totwt <= weight_limit else (0, 0)

    bagged = max(any_comb(items), key=total_value)  # max val or min wt if values equal
    if bagged[0].weight <= weight_limit:
        return bagged
    return []


# @profile
def knapsack_5_dynamic_solution(items: Tuple[Item], weight_limit: int) -> Item:
    """
    Dynamic programming solution
    http://rosettacode.org/mw/index.php?title=Knapsack_problem/0-1&action=edit&section=63
    """

    table = [[0] * (weight_limit + 1) for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, val, wt = items[j - 1]
        for w in range(1, weight_limit + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - wt] + val)

    w = weight_limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]
        if was_added:
            item, val, wt = items[j - 1]
            yield items[j - 1]
            w -= wt


# @profile
def knapsack_6_recursive_dynamic_solution(items: Tuple[Item], weight_limit: int) -> Tuple[Item]:
    """
    Recursive dynamic programming algorithm
    http://rosettacode.org/mw/index.php?title=Knapsack_problem/0-1&action=edit&section=64
    """

    def total_value(items: Tuple[Item], weight_limit: int) -> int:
        return sum([x.value for x in items]) if sum([x.weight for x in items]) <= weight_limit else 0

    cache = {}

    def solve(items: Tuple[Item], weight_limit: int) -> Tuple:
        if not items:
            return ()
        if (items, weight_limit) not in cache:
            head = items[0]
            tail = items[1:]
            include = (head,) + solve(tail, weight_limit - head[2])
            dont_include = solve(tail, weight_limit)
            if total_value(include, weight_limit) > total_value(dont_include, weight_limit):
                answer = include
            else:
                answer = dont_include
            cache[(items, weight_limit)] = answer
        return cache[(items, weight_limit)]

    return solve(items, weight_limit)


# @profile
def knapsack_greedy_solution(items: Tuple[Item], weight_limit: int) -> Iterator:
    """
    Return a list of items with the maximum value, subject to the
    constraint that their combined weight must not exceed max_weight.
    Implements the well-known "greedy approximation algorithm" for the knapsack problem
    (first described by George Dantzig in 1957).
    https://codereview.stackexchange.com/a/62871
    """

    def efficiency(item: Item) -> float:
        """Return efficiency of item (its value per unit weight)."""
        return float(item.value) / float(item.weight)

    def pack(item: Item) -> bool:
        # Attempt to pack item; return True if successful.
        if item.weight <= pack.max_weight:
            pack.max_weight -= item.weight
            return True
        else:
            return False

    pack.max_weight = weight_limit
    return filter(pack, sorted(items, key=efficiency, reverse=True))


if __name__ == '__main__':
    import time

    from data import pack_up_static_knapsack_3

    funcs = [
        knapsack_1_standard_solution,
        knapsack_2_solution,
        knapsack_3_solution,
        knapsack_4_bruteforce_solution,
        knapsack_5_dynamic_solution,
        knapsack_6_recursive_dynamic_solution,
        knapsack_greedy_solution
    ]

    for func in funcs:
        list(func(*pack_up_static_knapsack_3()))
        time.sleep(0.3)
