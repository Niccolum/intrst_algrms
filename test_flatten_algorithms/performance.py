import timeit
import json

from data import (
    generate_data, create_data_decreasing_depth, create_data_increasing_depth)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)


def mean(numbers):
    return sum(numbers) / len(numbers)

result = {'decrease': {}, 'increase': {}}
for data_example in generate_data():
    data = data_example[1]
    data = create_data_decreasing_depth(**data)

    current_func = data_example[0]
    result['decrease'][current_func] = {}

    result['decrease'][current_func]['niccolum_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000))

    result['decrease'][current_func]['tishka_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000))

    result['decrease'][current_func]['zart_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000))

    result['decrease'][current_func]['outer_flatten_1'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000))

    result['decrease'][current_func]['outer_flatten_2'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000))

    result['decrease'][current_func]['recursion_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000))

    result['decrease'][current_func]['tishka_flatten_with_stack'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000))

    result['decrease'][current_func]['recursive_flatten_like_tishka'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000))

for data_example in generate_data():
    data = data_example[1]
    data = create_data_increasing_depth(**data)

    current_func = data_example[0]
    result['increase'][current_func] = {}

    result['increase'][current_func]['niccolum_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000))

    result['increase'][current_func]['tishka_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000))

    result['increase'][current_func]['zart_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000))

    result['increase'][current_func]['outer_flatten_1'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000))

    result['increase'][current_func]['outer_flatten_2'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000))

    result['increase'][current_func]['recursion_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000))

    result['increase'][current_func]['tishka_flatten_with_stack'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000))

    result['increase'][current_func]['recursive_flatten_like_tishka'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000))

with open('performance.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)