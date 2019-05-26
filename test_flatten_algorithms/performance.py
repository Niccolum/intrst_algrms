import timeit
from data import (
    generate_data, create_data_decreasing_depth, create_data_increasing_depth)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)

print('Decrease testing')
for data_example in generate_data():

    print(data_example[0])
    data = data_example[1]
    data = create_data_decreasing_depth(**data)

    print('niccolum_flatten')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000))

    print('zart_flatten')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000))

    print('outer_flatten_1')
    print(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000))

    print('outer_flatten_2')
    print(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000))

    print('recursion_flatten')
    print(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten_with_stack')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000))

    print('recursive_flatten_like_tishka')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000))

print('Increase testing')
for data_example in generate_data():

    print(data_example[0])
    data = data_example[1]
    data = create_data_increasing_depth(**data)
    
    print('niccolum_flatten')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000))

    print('zart_flatten')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000))

    print('outer_flatten_1')
    print(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000))

    print('outer_flatten_2')
    print(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000))

    print('recursion_flatten')
    print(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000))

    print('tishka_flatten_with_stack')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000))

    print('recursive_flatten_like_tishka')
    print(timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000))