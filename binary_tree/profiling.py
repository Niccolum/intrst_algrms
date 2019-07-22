import types
from memprof import memprof

from funcs import SingleNodeClass, TwoNodeClass
from data import mindatalist, middledatalist, bigdatalist


@memprof(threshold=1024, plot=True)
def mindatalist_SingleNodeClass():
    instance = SingleNodeClass()
    for item in mindatalist:
        instance.add_node(item)
    result = instance.tree_data()


@memprof(threshold=1024, plot=True)
def middledatalist_SingleNodeClass():
    instance = SingleNodeClass()
    for item in middledatalist:
        instance.add_node(item)
    result = instance.tree_data()


@memprof(threshold=1024, plot=True)
def bigdatalist_SingleNodeClass():
    instance = SingleNodeClass()
    for item in bigdatalist:
        instance.add_node(item)
    result = instance.tree_data()


@memprof(threshold=1024, plot=True)
def mindatalist_TwoNodeClass():
    instance = TwoNodeClass()
    for item in mindatalist:
        instance.add_node(item)
    result = list(instance.tree_data())


@memprof(threshold=1024, plot=True)
def middledatalist_TwoNodeClass():
    instance = TwoNodeClass()
    for item in middledatalist:
        instance.add_node(item)
    result = list(instance.tree_data())


@memprof(threshold=1024, plot=True)
def bigdatalist_TwoNodeClass():
    instance = TwoNodeClass()
    for item in bigdatalist:
        instance.add_node(item)
    result = list(instance.tree_data())

mindatalist_SingleNodeClass()
middledatalist_SingleNodeClass()
bigdatalist_SingleNodeClass()

mindatalist_TwoNodeClass()
middledatalist_TwoNodeClass()
bigdatalist_TwoNodeClass()