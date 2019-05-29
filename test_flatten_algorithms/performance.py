import timeit
import json
import time

from data import (
    generate_data, create_data_decreasing_depth, create_data_increasing_depth)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)


def mean(numbers):
    return sum(numbers) / len(numbers)

result = {'decrease': {}, 'increase': {}}
print('*'*10, 'Decrease', '*'*10)
for data_example in generate_data():
    data = data_example[1]
    data = create_data_decreasing_depth(**data)

    current_func = data_example[0]
    print('\n', current_func, '\n')
    start = time.time()

    result['decrease'][current_func] = {}

    print('niccolum_flatten')
    result['decrease'][current_func]['niccolum_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten')
    result['decrease'][current_func]['tishka_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000))

    print('zart_flatten')
    result['decrease'][current_func]['zart_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000))

    print('outer_flatten_1')
    result['decrease'][current_func]['outer_flatten_1'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000))

    print('outer_flatten_2')
    result['decrease'][current_func]['outer_flatten_2'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000))

    print('recursion_flatten')
    result['decrease'][current_func]['recursion_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten_with_stack')
    result['decrease'][current_func]['tishka_flatten_with_stack'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000))

    print('recursive_flatten_like_tishka')
    result['decrease'][current_func]['recursive_flatten_like_tishka'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000))
    print('end {} time is {:.5f}'.format(current_func, time.time() - start))

print('*'*10, 'Increase', '*'*10)
for data_example in generate_data():
    data = data_example[1]
    data = create_data_increasing_depth(**data)

    current_func = data_example[0]
    print('\n', current_func, '\n')
    start = time.time()
    
    result['increase'][current_func] = {}

    print('niccolum_flatten')
    result['increase'][current_func]['niccolum_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten')
    result['increase'][current_func]['tishka_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000))

    print('zart_flatten')
    result['increase'][current_func]['zart_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000))

    print('outer_flatten_1')
    result['increase'][current_func]['outer_flatten_1'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000))

    print('outer_flatten_2')
    result['increase'][current_func]['outer_flatten_2'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000))

    print('recursion_flatten')
    result['increase'][current_func]['recursion_flatten'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten_with_stack')
    result['increase'][current_func]['tishka_flatten_with_stack'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000))

    print('recursive_flatten_like_tishka')
    result['increase'][current_func]['recursive_flatten_like_tishka'] = mean(
        timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000))

    print('end {} time is {:.5f}'.format(current_func, time.time() - start))

print('Done testing. Writes...')
with open('performance.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)
    print('Done')