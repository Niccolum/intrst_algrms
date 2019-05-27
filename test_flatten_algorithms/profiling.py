import sys
sys.setrecursionlimit(11000)

from data import (
    generate_data, create_data_decreasing_depth, create_data_increasing_depth)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)

from memory_profiler import show_results, LineProfiler

def args_eater(func_to_wrap): 
    @wraps(func_to_wrap) 
    def inner(*args, **kwargs): 
        return partial(func_to_wrap, *args, **kwargs) 
    return inner 

for data_example in generate_data():
    print('\n', data_example[0], '\n')
    data = data_example[1]
    data = create_data_decreasing_depth(**data)

    print('niccolum_flatten')
    prof = LineProfiler(backend='psutil')
    val = prof(niccolum_flatten)(data)
    show_results(prof, stream=None, precision=1)

    print('tishka_flatten')
    prof = LineProfiler(backend='psutil')
    val = prof(tishka_flatten)(data)
    show_results(prof, stream=None, precision=1)

    print('zart_flatten')
    prof = LineProfiler(backend='psutil')
    val = prof(zart_flatten)(data)
    show_results(prof, stream=None, precision=1)

    print('outer_flatten_1')
    prof = LineProfiler(backend='psutil')
    val = list(prof(outer_flatten_1)(data))
    show_results(prof, stream=None, precision=1)

    print('outer_flatten_2')
    prof = LineProfiler(backend='psutil')
    val = list(prof(outer_flatten_2)(data))
    show_results(prof, stream=None, precision=1)

    print('tishka_flatten_with_stack')
    prof = LineProfiler(backend='psutil')
    val = prof(tishka_flatten_with_stack)(data)
    show_results(prof, stream=None, precision=1)

    print('recursive_flatten_like_tishka')
    prof = LineProfiler(backend='psutil')
    val = prof(recursive_flatten_like_tishka)(data)
    show_results(prof, stream=None, precision=1)