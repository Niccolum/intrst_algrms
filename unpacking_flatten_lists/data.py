import math
import sys
from typing import List, Dict, Tuple, Union, Iterator
Num = Union[int, float]

sys.setrecursionlimit(11000)


def create_data_decreasing_depth(
        data: Union[List, Iterator],
        length: int,
        max_depth: int,
        _current_depth: int = None,
        _result: List = None
) -> List:
    """
    creates data in depth on decreasing.

    Examples:

    >>> data = create_data_decreasing_depth(list(range(1, 11)), length=5, max_depth=3)
    >>> assert data == [[[1, 2, 3, 4, 5], 6, 7, 8, 9, 10]]
    >>> data = create_data_decreasing_depth(list(range(1, 11)), length=2, max_depth=3)
    >>> assert data == [[[1, 2], 3, 4], 5, 6], [[7, 8,] 9, 10]]
    """
    _result = _result or []
    _current_depth = _current_depth or max_depth
    data = iter(data)
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
        data: Union[List, Iterator],
        length: int,
        max_depth: int,
        _current_depth: int = None,
        _result: List = None
) -> List:
    """
    creates data in depth to increase.

    Examples:

    >>> data = create_data_increasing_depth(list(range(1, 11)), length=5, max_depth=3)
    >>> assert data == [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
    >>> data = create_data_increasing_depth(list(range(1, 11)), length=2, max_depth=3)
    >>> assert data == [1, 2, [3, 4, [5, 6]]], 7, 8, [9, 10]]
    """
    _result = _result or []
    _current_depth = _current_depth or max_depth
    data = iter(data)
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

    if max_depth == _current_depth:
        tmp_res = create_data_increasing_depth(
            data=data,
            length=length,
            max_depth=max_depth)
        if tmp_res:
            _result += tmp_res
    return _result


def generate_data() -> List[Tuple[str, Dict[str, Union[range, Num]]]]:
    """
    Generated collections of Data by pattern

    {amount_item}_amount_{length}_length_{max_depth}_max_depth

    where:

    .. py:attribute:: amount_item:

        len of flatten elements

    .. py:attribute:: length:

        len of elements at the same level of nesting

    .. py:attribute:: max_depth:

        highest possible level of nesting
    """

    data = []
    amount_of_elements = [10 ** i for i in range(5)]
    data_template = '{amount_item}_amount_{length}_length_{max_depth}_max_depth'

    # amount_item doesn't need to be [1]
    for amount_item in amount_of_elements[1:]:
        for max_depth in amount_of_elements:
            # for exclude flatten list after generate data by create_data_increasing_depth
            if amount_item > max_depth:
                # generate four types of length
                for length in range(0, max_depth + 1, math.ceil(max_depth / 4)):
                    # min length must be 1
                    length = length or 1

                    data_name = data_template.format(
                        amount_item=amount_item,
                        length=length,
                        max_depth=max_depth
                    )

                    data_value = {
                        'data': range(amount_item),
                        'length': length,
                        'max_depth': max_depth
                    }

                    data.append((data_name, data_value))

                    # for not to produce more than 1 flat entity
                    if max_depth == 1:
                        break

    # this order is convenient for me
    data = sorted(data, key=lambda x: [x[1]['data'][-1], x[1]['max_depth'], x[1]['length']])
    return data


def get_data_name_order() -> List[str]:
    return [i[0] for i in generate_data()]


if __name__ == '__main__':
    for data in generate_data():
        print(data[0])
