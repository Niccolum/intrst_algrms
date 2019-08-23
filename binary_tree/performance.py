from collections import defaultdict
import timeit
import json
from contextlib import contextmanager
import time
from typing import List
from numbers import Integral

from binary_tree import BASEDIR
from binary_tree.funcs import SingleNodeClass, TwoNodeClass, BisectNodeClass
from binary_tree.data import datalist_100, datalist_1000, datalist_10000, datalist_100000, datalist_1000000

RETRY_NUM = 100
TOO_LONG = 60*2


def mean(numbers: List[Integral]) -> int:
    return sum(numbers) / len(numbers) / RETRY_NUM


@contextmanager
def time_time(msg: str) -> None:
    start = time.monotonic()
    yield start
    print('{} done: '.format(msg), time.monotonic() - start)


perf_classes = [SingleNodeClass, TwoNodeClass, BisectNodeClass]
perf_datalists = [datalist_100, datalist_1000, datalist_10000, datalist_100000, datalist_1000000]

result = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

fill_nodes_command = """
instance = Node()
for data in datalist:
    instance.add_node(data)
"""

print_node_list_command = """
result = list(instance.tree_data())
"""

setup_import_template = 'from __main__ import {cls_name} as Node, {datalist_name} as datalist'


def main():
    for cls in perf_classes:
        cls_name = cls.__name__
        print(cls_name)

        for datalist in perf_datalists:
            datalist_name = next(k for k, v in globals().items() if v == datalist)
            print(datalist_name)

            with time_time('add_node'):
                result[cls_name]['add_node'][datalist_name] = mean(
                    timeit.repeat(
                        fill_nodes_command,
                        setup=setup_import_template.format(cls_name=cls_name, datalist_name=datalist_name),
                        number=RETRY_NUM
                    )
                )

            with time_time('tree_data'):
                result[cls_name]['tree_data'][datalist_name] = mean(
                    timeit.repeat(
                        print_node_list_command,
                        setup=(setup_import_template + fill_nodes_command).format(
                            cls_name=cls_name, datalist_name=datalist_name
                        ),
                        number=RETRY_NUM
                    )
                )

            with time_time('full') as start_time:
                result[cls_name]['full'][datalist_name] = mean(
                    timeit.repeat(
                        (fill_nodes_command + print_node_list_command),
                        setup=setup_import_template.format(
                            cls_name=cls_name, datalist_name=datalist_name
                        ),
                        number=RETRY_NUM
                    )
                )
            if time.monotonic() - start_time > TOO_LONG:
                break

    with open(BASEDIR / 'performance.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)
        print('Done')


if __name__ == '__main__':
    main()
