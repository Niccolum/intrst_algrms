from memprof import memprof
from typing import List
from numbers import Integral

from funcs import BaseNodeClass


def abstract_wrapper(*, instance: BaseNodeClass, datalist: List[Integral]) -> list:
    for item in datalist:
        instance.add_node(item)
    return list(instance.tree_data())


@memprof(threshold=1024, plot=True)
def datalist_100_single_node_class() -> list:
    from funcs import SingleNodeClass
    from data import datalist_100
    return abstract_wrapper(instance=SingleNodeClass(), datalist=datalist_100)


@memprof(threshold=1024, plot=True)
def datalist_1000_single_node_class() -> list:
    from funcs import SingleNodeClass
    from data import datalist_1000
    return abstract_wrapper(instance=SingleNodeClass(), datalist=datalist_1000)


@memprof(threshold=1024, plot=True)
def datalist_10000_single_node_class() -> list:
    from funcs import SingleNodeClass
    from data import datalist_10000
    return abstract_wrapper(instance=SingleNodeClass(), datalist=datalist_10000)


@memprof(threshold=1024, plot=True)
def datalist_100000_single_node_class() -> list:
    from funcs import SingleNodeClass
    from data import datalist_100000
    return abstract_wrapper(instance=SingleNodeClass(), datalist=datalist_100000)


@memprof(threshold=1024, plot=True)
def datalist_1000000_single_node_class() -> list:
    from funcs import SingleNodeClass
    from data import datalist_1000000
    return abstract_wrapper(instance=SingleNodeClass(), datalist=datalist_1000000)


@memprof(threshold=1024, plot=True)
def datalist_100_two_node_class() -> list:
    from funcs import TwoNodeClass
    from data import datalist_100
    return abstract_wrapper(instance=TwoNodeClass(), datalist=datalist_100)


@memprof(threshold=1024, plot=True)
def datalist_1000_two_node_class() -> list:
    from funcs import TwoNodeClass
    from data import datalist_1000
    return abstract_wrapper(instance=TwoNodeClass(), datalist=datalist_1000)


@memprof(threshold=1024, plot=True)
def datalist_10000_two_node_class() -> list:
    from funcs import TwoNodeClass
    from data import datalist_10000
    return abstract_wrapper(instance=TwoNodeClass(), datalist=datalist_10000)


@memprof(threshold=1024, plot=True)
def datalist_100000_two_node_class() -> list:
    from funcs import TwoNodeClass
    from data import datalist_100000
    return abstract_wrapper(instance=TwoNodeClass(), datalist=datalist_100000)


@memprof(threshold=1024, plot=True)
def datalist_1000000_two_node_class() -> list:
    from funcs import TwoNodeClass
    from data import datalist_1000000
    return abstract_wrapper(instance=TwoNodeClass(), datalist=datalist_1000000)


if __name__ == '__main__':
    datalist_100_single_node_class()
    datalist_1000_single_node_class()
    datalist_10000_single_node_class()
    datalist_100000_single_node_class()
    datalist_1000000_single_node_class()

    datalist_100_two_node_class()
    datalist_1000_two_node_class()
    datalist_10000_two_node_class()
    datalist_100000_two_node_class()
    datalist_1000000_two_node_class()
