class Node:
    def __init__(self, data):
        self.__data = data
        self.__left_tree = None
        self.__right_tree = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_left_tree(self):
        return self.__left_tree

    def set_left_tree(self, tree):
        self.__left_tree = tree

    def get_right_tree(self):
        return self.__right_tree

    def set_right_tree(self, tree):
        self.__right_tree = tree

    def is_leaf(self):
        return self.get_left_tree() is self.get_right_tree() is None


class BinaryTree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def pre_order(self):
        def pre(node):
            if node is not None:
                print(node.get_data())
                pre(node.get_left_tree())
                pre(node.get_right_tree())
        pre(self.root)

    def in_order(self):
        def in_or(node):
            if node is not None:
                in_or(node.get_left_tree())
                print(node.get_data())
                in_or(node.get_right_tree())
        in_or(self.root)

    def post_order(self):
        def post(node):
            if node is not None:
                post(node.get_left_tree())
                post(node.get_right_tree())
                print(node.get_data())
        post(self.root)

    def insert(self, new_data):
        def ins(node, data):
            if node.get_data() > data:
                if node.get_left_tree() is None:
                    node.set_left_tree(Node(data))
                else:
                    ins(node.get_left_tree(), data)
            else:
                if node.get_right_tree() is None:
                    node.set_right_tree(Node(data))
                else:
                    ins(node.get_right_tree(), data)

        if self.empty():
            self.root = Node(new_data)
        else:
            ins(self.root, new_data)


binTree = BinaryTree()
binTree.insert(10)
binTree.insert(5)
binTree.insert(12)
binTree.insert(3)
binTree.insert(7)
binTree.insert(11)
binTree.insert(15)
binTree.in_order()
