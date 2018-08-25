class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        result = []
        if self.left:
            result.extend(list(self.left.print_tree()))
        result.append(self.data)
        if self.right:
            result.extend(list(self.right.print_tree()))
        return result


if __name__ == '__main__':
    main = Node(30)
    main.insert(10)
    main.insert(25)
    main.insert(15)
    main.insert(40)
    main.insert(50)
    main.insert(60)
    main.insert(3)
    main.insert(2)
    main.insert(1)

    print(main.print_tree())
