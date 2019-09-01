"""
Examples of python realization of solution for unpacking lists with indefinite depth
"""

from typing import Iterator, Iterable, List

from iteration_utilities import deepflatten
from more_itertools import collapse


# @profile
def outer_flatten_1(array: Iterable) -> List:
    """
    Based on C realization of this solution
    More on:

    https://iteration-utilities.readthedocs.io/en/latest/generated/deepflatten.html

    https://github.com/MSeifert04/iteration_utilities/blob/384948b4e82e41de47fa79fb73efc56c08549b01/src/deepflatten.c
    """
    return deepflatten(array)


# @profile
def outer_flatten_2(array: Iterable) -> List:
    """
    recursive algorithm, vaguely reminiscent of recursion_flatten. Based on next pattern:

    .. code:: python

        try:
            tree = iter(node)
        except TypeError:
            yield node

    more on:
    https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.collapse
    """
    return collapse(array)


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
def recursive_flatten_generator(array: Iterable) -> List:
    """
    Recursive algorithm
    Looks like recursive_flatten_iterator, but with extend/append

    """
    lst = []
    for i in array:
        if isinstance(i, list):
            lst.extend(recursive_flatten_generator(i))
        else:
            lst.append(i)
    return lst


# @profile
def recursive_flatten_iterator(arr: Iterable) -> Iterator:
    """
    Recursive algorithm based on iterator
    Usual solution to this problem

    """

    for i in arr:
        if isinstance(i, list):
            yield from recursive_flatten_iterator(i)
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


if __name__ == '__main__':

    import time

    from data import generate_data, create_data_increasing_depth, create_data_decreasing_depth


    def profile():
        all_data = generate_data()[-1][1]
        curr_data = all_data[-1][1]

        funcs_generated_data = [
            create_data_increasing_depth,
            create_data_decreasing_depth
        ]

        funcs = [
            outer_flatten_1,
            outer_flatten_2,
            niccolum_flatten,
            tishka_flatten,
            zart_flatten,
            recursive_flatten_generator,
            recursive_flatten_iterator,
            tishka_flatten_with_stack
        ]

        for func_generated_data in funcs_generated_data:
            creating_data = func_generated_data(**curr_data)
            for func in funcs:
                list(func(creating_data))
                time.sleep(0.3)

    profile()
