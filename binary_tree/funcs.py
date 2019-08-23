"""
Examples of binary tree, made in the style of OOP

It's just example of binary sort functions, based or not on his own tree.
"""

from abc import ABCMeta, abstractmethod
from collections.abc import Iterator
from numbers import Integral
import bisect


class BaseNodeClass(metaclass=ABCMeta):
    """
    Abstract Binary Tree Class
    All other based on this interface
    """

    @abstractmethod
    def add_node(self, *args) -> None:
        """
        add items to data container
        """
        raise NotImplementedError

    @abstractmethod
    def tree_data(self) -> Iterator:
        """
        return sorted items of inner data
        """
        raise NotImplementedError


class BisectNodeClass(BaseNodeClass):
    """
    Based on bisect stdlib, without inner tree
    """
    def __init__(self):
        self.data = []

    # @profile
    def add_node(self, data: Integral) -> None:
        bisect.insort(self.data, data)

    # @profile
    def tree_data(self) -> Iterator:
        yield from self.data


class SingleNodeClass(BaseNodeClass):
    """
    All operations and storage takes place inside one class
    """

    def __init__(self, data: Integral = None):
        self.left = None
        self.right = None
        self.data = data

    # @profile
    def add_node(self, data: Integral) -> None:
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = SingleNodeClass(data)
                else:
                    self.left.add_node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = SingleNodeClass(data)
                else:
                    self.right.add_node(data)
        else:
            self.data = data

    # @profile
    def tree_data(self) -> Iterator:
        if self.left:
            yield from self.left.tree_data()
        yield self.data
        if self.right:
            yield from self.right.tree_data()


class TwoNodeClass(BaseNodeClass):
    """
    Use inner class Node for storage and TwoNodeClass for for everything else
    based on https://gist.github.com/samidhtalsania/6659380
    """

    class Node:
        """
        Inner class of item, which contain info about neightbours
        """
        def __init__(self, key: Integral):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    # @profile
    def add_node(self, key: Integral, _node: Node = None) -> None:

        if _node is None:
            _node = self.root

        if self.root is None:
            self.root = self.Node(key)

        else:
            if key <= _node.key:
                if _node.left is None:
                    _node.left = self.Node(key)
                    _node.left.parent = _node
                    return
                else:
                    return self.add_node(key, _node=_node.left)
            else:
                if _node.right is None:
                    _node.right = self.Node(key)
                    _node.right.parent = _node
                    return
                else:
                    return self.add_node(key, _node=_node.right)

    # @profile
    def tree_data(self, node: Node = None) -> Iterator:
        if node is None:
            node = self.root

        stack = []
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.key
                node = node.right


if __name__ == '__main__':
    import time

    from data import datalist_100

    def profile():
        nodes = [SingleNodeClass, TwoNodeClass, BisectNodeClass]
        for cls_node in nodes:
            node = cls_node()
            for i in datalist_100:
                node.add_node(i)
            list(node.tree_data())
            del node
            time.sleep(0.3)

    profile()
