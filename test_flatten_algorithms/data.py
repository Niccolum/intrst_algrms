import math
import sys
sys.setrecursionlimit(2000)


def create_data_decreasing_depth(
    data: list,
    length: int,
    max_depth: int,
    _curr_len: int,
    _curr_depth: int,
    _result: int
):
    '''
    creates data in depth on decreasing
    examples:
    data=list(range(1, 11)), length=5, max_depth=3 => [[[1, 2, 3, 4, 5], 6, 7, 8, 9, 10]]
    data=list(range(1, 11)), length=2, max_depth=3 => [[[1, 2], 3, 4], 5, 6], [[7, 8,] 9, 10]]
    '''
    ...


def create_data_increasing_depth(
    data: list,
    length: int,
    max_depth: int,
    _curr_len: int,
    _curr_depth: int,
    _result: int
):
    '''
    creates data in depth to increase
    examples:
    data=list(range(1, 11)), length=5, max_depth=3 => [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
    data=list(range(1, 11)), length=2, max_depth=3 => [1, 2, [3, 4, [5, 6]]], 7, 8, [9, 10]]
    '''
    ...


def create_data(data=None, length=1, _curr_length=None, _result=None):

    result = _result or []
    _curr_length = _curr_length or length
    res = []

    while _curr_length:
        try:
            item = next(data)
            res.append(item)
        except StopIteration:
            if res:
                result.append(res)
            return result
        except TypeError:
            print('incorrect data. Must be iter(range(...))')
        _curr_length -= 1
    result.append(create_data(data=data, _result=res, length=length))
    return result


def generate_data():
    difficult_ratio = dict(
        _easy=1,
        __medium=0.7,
        ___hard=0,
    )

    length = dict(
        _short=10,
        __middle=100,
        ___long=1000,
        ____lengthy=10000
    )

    deep = dict(
        _small=1,
        __medium=10,
        ___big=100,
        ____very_big=1000
    )

    get_data = sorted([
        ('{}{}{}'.format(len_k, diff_k, deep_k), {
            'data': list(range(len_v)),
            'length': math.ceil(len_v ** diff_v),
            'max_deep': deep_v
        })
        for len_k, len_v in length.items()
        for diff_k, diff_v in difficult_ratio.items()
        for deep_k, deep_v in deep.items()
    ], reverse=True)
    return get_data


if __name__ == '__main__':
    for i in generate_data():
        print(i)
