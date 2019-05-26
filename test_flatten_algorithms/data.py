import math
import sys
sys.setrecursionlimit(2000)


def create_data_decreasing_depth(
    data: list,
    length: int,
    max_depth: int,
    _current_depth: int = None,
    _result: list = None
):
    '''
    creates data in depth on decreasing
    examples:
    data=iter(range(1, 11)), length=5, max_depth=3 => [[[1, 2, 3, 4, 5], 6, 7, 8, 9, 10]]
    data=iter(range(1, 11)), length=2, max_depth=3 => [[[1, 2], 3, 4], 5, 6], [[7, 8,] 9, 10]]
    '''
    _result = _result or []
    _current_depth = _current_depth or max_depth
    if _current_depth - 1:
        _result.append(create_data_decreasing_depth(
            data=data,
            length=length,
            max_depth=max_depth,
            _current_depth=_current_depth - 1,
            _result=_result))
    try:
        _current_length = length
        while _current_length:
            item = next(data)
            _result.append(item)
            _current_length -= 1
        
        if max_depth == _current_depth:
            _result += create_data_decreasing_depth(
                data=data,
                length=length,
                max_depth=max_depth)
        return _result

    except StopIteration:
        return _result


def create_data_increasing_depth(
    data: list,
    length: int,
    max_depth: int,
    _current_depth: int = None,
    _result: list = None
):
    '''
    creates data in depth to increase
    examples:
    data=list(range(1, 11)), length=5, max_depth=3 => [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
    data=list(range(1, 11)), length=2, max_depth=3 => [1, 2, [3, 4, [5, 6]]], 7, 8, [9, 10]]
    '''
    _result = _result or []
    _current_depth = _current_depth or max_depth
    try:
        _current_length = length
        while _current_length:
            item = next(data)
            _result.append(item)
            _current_length -= 1

    except StopIteration:
        return _result

    if _current_depth - 1:
        tmp_res = create_data_increasing_depth(
            data=data,
            length=length,
            max_depth=max_depth,
            _current_depth=_current_depth - 1)
        if tmp_res:
            _result.append(tmp_res)
    else:
        return _result

    if max_depth == _current_depth:
        tmp_res = create_data_increasing_depth(
            data=data,
            length=length,
            max_depth=max_depth)
        if tmp_res:
            _result += tmp_res
    return _result


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
            'data': iter(range(len_v)),
            'length': math.ceil(len_v ** diff_v),
            'max_deep': deep_v
        })
        for len_k, len_v in length.items()
        for diff_k, diff_v in difficult_ratio.items()
        for deep_k, deep_v in deep.items()
    ], reverse=True)
    return get_data
