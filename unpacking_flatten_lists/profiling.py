from functools import wraps
import sys
sys.setrecursionlimit(2000)

from data import (
    generate_data, create_data_decreasing_depth, create_data_increasing_depth)
from funcs import (
    outer_flatten_1, outer_flatten_2, niccolum_flatten, 
    tishka_flatten, zart_flatten, recursion_flatten, tishka_flatten_with_stack,
    recursive_flatten_like_tishka)

from memprof import memprof

def data_generator_wrapper(func):
    @wraps(func)
    def wrapper():
        for data_example in generate_data():
            data_args = data_example[1]
            data = create_data_decreasing_depth(**data_args)
            func(data)
            data = create_data_increasing_depth(**data_args)
            func(data)
        return
    return wrapper

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_outer_flatten_1(data):
    return list(outer_flatten_1(data))

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_outer_flatten_2(data):
    return list(outer_flatten_2(data))

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_niccolum_flatten(data):
    return niccolum_flatten(data)

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_tishka_flatten(data):
    return tishka_flatten(data)

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_zart_flatten(data):
    return zart_flatten(data)

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_recursion_flatten(data):
    return list(recursion_flatten(data))

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_tishka_flatten_with_stack(data):
    return tishka_flatten_with_stack(data)

@memprof(threshold=1024, plot=True)
@data_generator_wrapper
def profile_recursive_flatten_like_tishka(data):
    return recursive_flatten_like_tishka(data)


profile_niccolum_flatten()

profile_tishka_flatten()

profile_zart_flatten()

profile_outer_flatten_1()

profile_outer_flatten_2()

profile_recursion_flatten()

profile_tishka_flatten_with_stack()

profile_recursive_flatten_like_tishka()