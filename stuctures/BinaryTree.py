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

    def n_child(self):
        res = 0
        if self.get_left_tree() is not None:
            res += 1
        if self.get_right_tree() is not None:
            res += 1
        return res

    def __str__(self):
        return f"Node: {str(self.get_data())}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def empty(self):
        return self.root is None

    def pre_order(self):
        def pre(node, lis):
            if node is not None:
                lis.append(node.get_data())
                pre(node.get_left_tree(), lis)
                pre(node.get_right_tree(), lis)
            return lis
        if self.empty():
            raise Exception()
        else:
            return pre(self.root, [])

    def in_order(self):
        def in_or(node, lis):
            if node is not None:
                in_or(node.get_left_tree(), lis)
                lis.append(node.get_data())
                in_or(node.get_right_tree(), lis)
            return lis
        if self.empty():
            raise Exception()
        else:
            return in_or(self.root, [])

    def post_order(self):
        def post(node, lis):
            if node is not None:
                post(node.get_left_tree(), lis)
                post(node.get_right_tree(), lis)
                lis.append(node.get_data())
            return lis
        if self.empty():
            raise Exception()
        else:
            return post(self.root, [])

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

    def search(self, search_data):
        def see(node, data):
            if node is None:
                raise Exception("No such data")
            if node.get_data() == data:
                return node
            else:
                if node.get_data() > data:
                    return see(node.get_left_tree(), data)
                else:
                    return see(node.get_right_tree(), data)

        if self.empty():
            raise Exception("Empty tree")
        else:
            return see(self.root, search_data)

    def delete(self, delete_data):
        def del_data(node, data):
            if node is None:
                raise Exception("No such data")

            elif node.get_left_tree().get_data() == data:
                deleted = node.get_left_tree()
                if deleted.n_child() == 0:
                    node.set_left_tree(None)
                    return deleted

                elif deleted.n_child() == 1:
                    new = None
                    if deleted.get_left_tree() is not None:
                        new = deleted.get_left_tree()
                    else:
                        new = deleted.get_right_tree()
                    node.set_left_tree(new)
                    return deleted

            elif node.get_right_tree().get_data() == data:
                deleted = node.get_right_tree()
                if deleted.n_child() == 0:
                    node.set_left_tree(None)
                    return deleted

                elif deleted.n_child() == 1:
                    new = None
                    if deleted.get_left_tree() is not None:
                        new = deleted.get_left_tree()
                    else:
                        new = deleted.get_right_tree()
                    node.set_right_tree(new)
                    return deleted

            else:
                if node.get_data() > data:
                    return del_data(node.get_left_tree(), data)
                else:
                    return del_data(node.get_right_tree(), data)

        if self.empty():
            raise Exception()
        else:
            return del_data(self.root, delete_data)


binTree = BinaryTree()
binTree.insert(10)
binTree.insert(5)
binTree.insert(12)
binTree.insert(3)
binTree.insert(11)
# binTree.insert(15)

print(binTree.pre_order())
print(binTree.delete(12))
print(binTree.pre_order())
