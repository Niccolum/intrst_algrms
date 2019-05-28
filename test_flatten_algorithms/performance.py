import timeit
import logging
from data import (
    generate_data, create_data_decreasing_depth, create_data_increasing_depth)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)

logging.basicConfig(
    level=logging.DEBUG, 
    filename='performance.log', 
    format='%(message)s')

def mean(numbers):
    return sum(numbers) / len(numbers)

logging.debug('*'*10+'Decrease testing'+'*'*10)
for data_example in generate_data():

    logging.debug(data_example[0])
    data = data_example[1]
    data = create_data_decreasing_depth(**data)

    logging.debug('niccolum_flatten')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000)))

    logging.debug('tishka_flatten')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000)))

    logging.debug('zart_flatten')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000)))

    logging.debug('outer_flatten_1')
    logging.debug(mean(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000)))

    logging.debug('outer_flatten_2')
    logging.debug(mean(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000)))

    logging.debug('recursion_flatten')
    logging.debug(mean(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000)))

    logging.debug('tishka_flatten_with_stack')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000)))

    logging.debug('recursive_flatten_like_tishka')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000)))

logging.debug('*'*10+'Increase testing'+'*'*10)
for data_example in generate_data():

    logging.debug(data_example[0])
    data = data_example[1]
    data = create_data_increasing_depth(**data)
    
    logging.debug('niccolum_flatten')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import niccolum_flatten as flatten, data', 
        number=10000)))

    logging.debug('tishka_flatten')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten as flatten, data', 
        number=10000)))

    logging.debug('zart_flatten')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import zart_flatten as flatten, data', 
        number=10000)))

    logging.debug('outer_flatten_1')
    logging.debug(mean(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_1 as flatten, data', 
        number=10000)))

    logging.debug('outer_flatten_2')
    logging.debug(mean(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import outer_flatten_2 as flatten, data', 
        number=10000)))

    logging.debug('recursion_flatten')
    logging.debug(mean(timeit.repeat(
        'list(flatten(data))', 
        'from __main__ import recursion_flatten as flatten, data', 
        number=10000)))

    logging.debug('tishka_flatten_with_stack')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import tishka_flatten_with_stack as flatten, data', 
        number=10000)))

    logging.debug('recursive_flatten_like_tishka')
    logging.debug(mean(timeit.repeat(
        'flatten(data)', 
        'from __main__ import recursive_flatten_like_tishka as flatten, data', 
        number=10000)))