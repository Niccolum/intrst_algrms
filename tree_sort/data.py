"""
Generate test data for test performance
"""
from typing import List
from random import shuffle


def generate_data(num: int) -> List[int]:
    """
    generate data numbers in random order
    result -> "datalist_*num*"
    """
    data = list(range(num))
    shuffle(data)
    return data


datalist_100 = generate_data(100)
datalist_1000 = generate_data(1000)
datalist_10000 = generate_data(10000)
datalist_100000 = generate_data(100000)
datalist_1000000 = generate_data(1000000)