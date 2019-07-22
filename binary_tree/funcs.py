class SingleNodeClass:
    # default node

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def add_node(self, data):
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

    def tree_data(self):
        result = []
        if self.left:
            result.extend(list(self.left.tree_data()))
        result.append(self.data)
        if self.right:
            result.extend(list(self.right.tree_data()))
        return result


class TwoNodeClass():
    # based on https://gist.github.com/samidhtalsania/6659380

    class Node():

        def __init__(self,key):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None        

    def add_node(self,key,node=None):

        if node is None:
            node = self.root
        
        if self.root is None:
            self.root = self.Node(key)

        else:
            if key <= node.key :
                if node.left is None:
                    node.left = self.Node(key)
                    node.left.parent = node
                    return 
                else:
                    return self.add_node(key,node = node.left)
            else:
                if node.right is None:
                    node.right = self.Node(key)
                    node.right.parent = node
                    return 
                else:
                    return self.add_node(key,node = node.right)

    def tree_data(self,node=None):
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

    main = TwoNodeClass()
    for i in data.mindatalist:
        main.add_node(i)

    print(list(main.tree_data()) == sorted(data.mindatalist))
