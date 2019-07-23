"""
Examples of binary tree, made in the style of OOP, which realize next functionality:
add_node: add new element to our tree
tree_data: return sorted list of inner data
"""


class SingleNodeClass:
    # default single node

    def __init__(self, data: 'SingleNodeClass' = None):
        self.left = None
        self.right = None
        self.data = data

    def add_node(self, data: 'SingleNodeClass'):
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

    def tree_data(self) -> list:
        result = []
        if self.left:
            result.extend(list(self.left.tree_data()))
        result.append(self.data)
        if self.right:
            result.extend(list(self.right.tree_data()))
        return result


class TwoNodeClass:
    # based on https://gist.github.com/samidhtalsania/6659380

    class Node:

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def add_node(self, key, node=None):

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

    def tree_data(self, node=None):
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
    import data

    snc = SingleNodeClass()
    for i in data.min_datalist:
        snc.add_node(i)

    print(list(snc.tree_data()) == sorted(data.min_datalist))

    tnc = TwoNodeClass()
    for i in data.min_datalist:
        tnc.add_node(i)

    print(list(tnc.tree_data()) == sorted(data.min_datalist))
