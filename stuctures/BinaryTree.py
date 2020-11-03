class Node:
    def __init__(self, data):
        self.__data = data
        self.__left_tree = None
        self.__right_tree = None
        self.__parent = None

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

    def get_parent(self):
        return self.__parent

    def set_parent(self, new_parent):
        self.__parent = new_parent

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
            raise Exception("Empty Tree")
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
        def ins(node, new_node):
            if node.get_data() > new_node.get_data():
                if node.get_left_tree() is None:
                    node.set_left_tree(new_node)
                    new_node.set_parent(node)
                else:
                    ins(node.get_left_tree(), new_node)
            else:
                if node.get_right_tree() is None:
                    node.set_right_tree(new_node)
                    new_node.set_parent(node)
                else:
                    ins(node.get_right_tree(), new_node)

        if self.empty():
            self.root = Node(new_data)
        else:
            ins(self.root, Node(new_data))

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

    def previous_element(self, data):
        def previous(node):
            if node.get_left_tree():
                return right_desc(node)
            else:
                return left_ancestor(node)

        def right_desc(node):
            node_ref = node.get_left_tree()
            while node_ref.get_right_tree():
                node_ref = node_ref.get_right_tree()
            return node_ref

        def left_ancestor(node):
            if node.get_parent().get_data() < node.get_data():
                return node.get_parent()
            else:
                return left_ancestor(node.get_parent())

        return previous(self.search(data))

    def array_to_bst(self, new_array_nums):
        def array(arr):
            arr.sort()
            if not arr:
                return None
            mid = (len(arr)) // 2
            root = Node(arr[mid])
            root.set_left_tree(array(arr[:mid]))
            root.set_right_tree(array(arr[mid+1:]))
            return root

        self.root = array(new_array_nums)


# Caso de prueba 1
binTree = BinaryTree()
arr = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
binTree.array_to_bst(arr)
print(binTree.in_order())

#Caso de prueba 2
binTree2 = BinaryTree()
arr = [6, 9, 4, 2, 3, 7, 11, 15, 12, 10, 1, 13]
binTree2.array_to_bst(arr)
print(binTree2.in_order())
