import timeit
from data import generate_data, create_data
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack)

for data_example in generate_data():
    print(data_example)
    data = data_example[1]
    data = create_data(data=iter(data['data']), length=data['length'])
    print('niccolum_flatten')
    print(timeit.repeat('flatten(data)', 'from __main__ import niccolum_flatten as flatten, data', number=10000))
    print('tishka_flatten')
    print(timeit.repeat('flatten(data)', 'from __main__ import tishka_flatten as flatten, data', number=10000))
    print('zart_flatten')
    print(timeit.repeat('flatten(data)', 'from __main__ import zart_flatten as flatten, data', number=100000))
    print('outer_flatten_1')
    print(timeit.repeat('flatten(data)', 'from __main__ import outer_flatten_1 as flatten, data', number=100000))
    print('outer_flatten_2')
    print(timeit.repeat('flatten(data)', 'from __main__ import outer_flatten_2 as flatten, data', number=100000))
    print('recursion_flatten')
    print(timeit.repeat('flatten(data)', 'from __main__ import recursion_flatten as flatten, data', number=100000))
    print('tishka_flatten_with_stack')
    print(timeit.repeat('flatten(data)', 'from __main__ import tishka_flatten_with_stack as flatten, data', number=100000))