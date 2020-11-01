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

    def have(self, have_data):
        try:
            self.search(have_data)
            return True
        except:
            return False

    def remove(self, data):

        if self.root is None:
            return False

        if self.root.get_data() == data:

            if self.root.is_leaf():
                deleted = self.root
                self.root = None
                return deleted

            elif self.root.get_left_tree() and self.root.get_right_tree() is None:
                deleted = self.root
                self.root = self.root.get_left_tree()
                return deleted

            elif self.root.get_left_tree() is None and self.root.get_right_tree():
                deleted = self.root()
                self.root = self.root.get_right_tree()
                return deleted
            # Case 2.4: Root node has two children
            else:
                move_node = self.root.get_right_tree()
                move_node_parent = None
                while move_node.get_left_tree():
                    move_node_parent = move_node
                    move_node = move_node.left
                self.root.get_data(move_node.data)
                if move_node.data < move_node_parent.data:
                    move_node_parent.left = None
                else:
                    move_node_parent.right = None
                return True
        # Find node to remove
        parent = None
        node = self.root
        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
        # Case 3: Node not found
        if node == None or node.data != data:
            return False
        # Case 4: Node has no children
        elif node.left is None and node.right is None:
            if data < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        # Case 5: Node has left child only
        elif node.left and node.right is None:
            if data < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        # Case 6: Node has right child only
        elif node.left is None and node.right:
            if data < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        # Case 7: Node has left and right child
        else:
            move_node_parent = node
            move_node = node.right
            while move_node.left:
                move_node_parent = move_node
                move_node = move_node.left
            node.data = move_node.data
            if move_node.right:
                if move_node.data < move_node_parent.data:
                    move_node_parent.left = move_node.right
                else:
                    move_node_parent.right = move_node.right
            else:
                if move_node.data < move_node_parent.data:
                    move_node_parent.left = None
                else:
                    move_node_parent.right = None
            return True


binTree = BinaryTree()
binTree.insert(10)
binTree.insert(5)
binTree.insert(3)
binTree.insert(6)

# binTree.insert(15)

print(binTree.in_order())
print(binTree.remove(10))
print(binTree.in_order())
