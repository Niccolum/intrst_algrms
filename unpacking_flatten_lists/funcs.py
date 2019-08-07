from typing import Iterator, Iterable, List

from iteration_utilities import deepflatten as outer_flatten_1
from more_itertools import collapse as outer_flatten_2


# @profile
def niccolum_flatten(array: Iterable) -> List:
    """
    Non recursive algorithm
    Based on pop/insert elements in current list
    """

    new_array = array[:]
    ind = 0
    while True:
        try:
            while isinstance(new_array[ind], list):
                item = new_array.pop(ind)
                for inner_item in reversed(item):
                    new_array.insert(ind, inner_item)
            ind += 1
        except IndexError:
            break
    return new_array


# @profile
def tishka_flatten(data: Iterable) -> List:
    """
    Non recursive algorithm
    Based on append/extend elements to new list

    """
    nested = True
    while nested:
        new = []
        nested = False
        for i in data:
            if isinstance(i, list):
                new.extend(i)
                nested = True
            else:
                new.append(i)
        data = new
    return data


# @profile
def zart_flatten(a: Iterable) -> List:
    """
    Non recursive algorithm
    Based on pop from old and append elements to new list
    """
    queue, out = [a], []
    while queue:
        elem = queue.pop(-1)
        if isinstance(elem, list):
            queue.extend(elem)
        else:
            out.append(elem)
    return out[::-1]


# @profile
def recursive_flatten_like_tishka(array: Iterable) -> List:
    """
    Recursive algorithm
    Based on tishka_flatten algorithm

    """
    lst = []
    for i in array:
        if isinstance(i, list):
            lst.extend(recursive_flatten_like_tishka(i))
        else:
            lst.append(i)
    return lst


# @profile
def recursion_flatten(arr: Iterable) -> Iterator:
    """
    Recursive algorithm based on iterator
    Usual solution to this problem

    """

    for i in arr:
        if isinstance(i, list):
            yield from recursion_flatten(i)
        else:
            yield i


# @profile
def tishka_flatten_with_stack(seq: Iterable) -> List:
    """
    Non recursive algorithm
    Based on zart_flatten, but build on try/except pattern
    """
    stack = [iter(seq)]
    new = []
    while stack:
        i = stack.pop()
        try:
            while True:
                data = next(i)
                if isinstance(data, list):
                    stack.append(i)
                    i = iter(data)
                else:
                    new.append(data)
        except StopIteration:
            pass
    return new
