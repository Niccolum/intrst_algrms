from iteration_utilities import deepflatten as outer_flatten_1
from more_itertools import collapse as outer_flatten_2


def niccolum_flatten(array):
    new_array = array[:]
    ind = 0
    while True:
        try:
            if isinstance(new_array[ind], list):
                item = new_array.pop(ind)
                for inneritem in reversed(item):
                    new_array.insert(ind, inneritem)
            else:
                new_array.insert(ind, array[ind])
                ind += 1
        except IndexError:
            break
    return new_array


def tishka_flatten(data):
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
    return new


def zart_flatten(a):
    queue, out = [a], []
    while queue:
        elem = queue.pop(-1)
        if isinstance(elem, list):
            queue.extend(elem)
        else:
            out.append(elem)
    return out[::-1]


def recursion_flatten(a):
    for i in arr:
        if isintance(i, list):
            yield from flatten(arr)
        else:
            yield i

def tishka_flatten_with_stack(seq):
    stack=[iter(seq)]
    new=[]
    while stack:
        i=stack.pop()
        try:
            while True:
                data=next(i)
                if isinstance(data, list):
                    stack.append(i)
                    i=iter(data)
                else:
                    new.append(data)
        except StopIteration:
            pass
    return new