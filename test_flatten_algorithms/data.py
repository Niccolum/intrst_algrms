import math
import sys
sys.setrecursionlimit(11000)

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
        short=10,
        middle=100,
        long=1000,
        lengthy=10000
    )

    get_data = [
        ('{}{}'.format(len_k, diff_k), {
            'data': range(len_v),
            'length': math.ceil(len_v ** diff_v)
        })
        for len_k, len_v in length.items()
        for diff_k, diff_v in difficult_ratio.items()
    ]
    data = sorted(get_data, reverse=True)
    return data

if __name__ == '__main__':
    print(generate_data())