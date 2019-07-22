import timeit
import json
import time

from funcs import SingleNodeClass, TwoNodeClass
# from data import mindatalist, middledatalist, bigdatalist
from data import mindatalist

def mean(numbers):
    return sum(numbers) / len(numbers)

perf_funcs = [SingleNodeClass, TwoNodeClass]
# perf_datalists = [mindatalist, middledatalist, bigdatalist]
perf_datalists = [mindatalist]

result = dict.fromkeys([i.__name__ for i in perf_funcs])

def main():
    for func in perf_funcs:
        func_result = result[func.__name__]
        for datalist in perf_datalists:
            data_res = [k for k, v in globals().items() if v == datalist]
            print(data_res)

if __name__ == '__main__':
    main()