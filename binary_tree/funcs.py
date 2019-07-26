"""
Examples of binary tree, made in the style of OOP, which realize next functionality:
add_node: add new element to our tree
tree_data: return sorted list of inner data

Next classes are implemented:
BaseNodeClass: abstract Binary Tree Class
SingleNodeClass: all operations and storage takes place inside one class
TwoNodeClass: use inner class Node for storage and TwoNodeClass for for everything else
"""

from abc import ABCMeta, abstractmethod
from collections.abc import Iterator
from numbers import Integral


class BaseNodeClass(metaclass=ABCMeta):

    @abstractmethod
    def add_node(self, *args) -> None:
        raise NotImplementedError

    @abstractmethod
    def tree_data(self) -> Iterator:
        raise NotImplementedError


class SingleNodeClass(BaseNodeClass):

    def __init__(self, data: Integral = None):
        self.left = None
        self.right = None
        self.data = data

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

    def tree_data(self) -> Iterator:
        if self.left:
            yield from self.left.tree_data()
        yield self.data
        if self.right:
            yield from self.right.tree_data()


class TwoNodeClass(BaseNodeClass):
    # based on https://gist.github.com/samidhtalsania/6659380

    class Node:

        def __init__(self, key: Integral):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def add_node(self, key: Integral, node: Node = None) -> None:

        if node is None:
            node = self.root

        if self.root is None:
            self.root = self.Node(key)

        else:
            if key <= node.key:
                if node.left is None:
                    node.left = self.Node(key)
                    node.left.parent = node
                    return
                else:
                    return self.add_node(key, node=node.left)
            else:
                if node.right is None:
                    node.right = self.Node(key)
                    node.right.parent = node
                    return
                else:
                    return self.add_node(key, node=node.right)

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