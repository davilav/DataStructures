import copy


class BinaryHeap(object):
    def __init__(self, heap):
        self.heap = copy.deepcopy(heap)
        if self.heap:
            self.heapify()

    def elements(self):
        """
        Method to return elements of Binary Heap
        """
        return self.heap

    def length(self):
        """
        Method to return length of Binary Heap
        """
        return len(self.heap)

    def heapify(self):
        """
        Brief:
            Method to convert Array into Binary Heap
        Args:
        #    heap: Array to be converted
        """
        size = self.length()
        for index in reversed(range(size // 2)):
            self._heapify(index=index, size=size)

    def swim_up(self, index):
        self._swim_up(index=index)

    def get_root_value(self):
        """
        Return root value of the heap
        """
        return self.heap[0]

    def add_element(self, element):
        """
        Brief:
            Method to add element / elements to heap
        Args:
            element: Could be a single number of array of numbers
        """
        if isinstance(element, list):
            for _element in element:
                self.heap.append(_element)
                self.swim_up(self.length())
        else:
            self.heap.append(element)
            self.swim_up(self.length())

    def extract_root(self):
        """
        Remove root element from the heap and return it
        """
        self._swap(0, self.length() - 1)
        result = self.heap.pop()
        self._heapify(index=0, size=self.length())
        return result

    def search_value(self, value):
        """
        Brief:
            Searches the value in heap and returns index
        Args:
            value: The value to be searched in the heap
        Return:
             Returns the index if the value is found otherwise -1
             Note: if same element is present multiple times,
                   first occurring index is returned
        """
        size = self.length()
        for index in range(0, size):
            if self.heap[index] == value:
                return index

        return -1

    def _swap(self, index1, index2):
        """
        Brief:
            Swap two elements in the given heap
        Args:
            index1: Index of the 1st element to be swapped
            index2: Index of the 2nd element to be swapped
        """
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def _left_child_index(self, index):
        """
        Method to get the left child index of any given node
        """
        return (2 * index) + 1

    def _right_child_index(self, index):
        """
        Method to get the right child index of any given node
        """
        return (2 * index) + 2


class MaxHeap(BinaryHeap):
    def __init__(self, heap=[]):
        super(self.__class__, self).__init__(heap=heap)

    def _heapify(self, index, size):
        """
        Brief:
            Private method to shift-up the smallest number
        Args:
            heap: Unprocessed Array
            index: Index to start
            size: Size of the array
        """

        l_index = self._left_child_index(index)
        r_index = self._right_child_index(index)
        largest_index = index
        if l_index < size and self.heap[l_index] > self.heap[index]:
            largest_index = l_index
        if r_index < size and self.heap[r_index] > self.heap[largest_index]:
            largest_index = r_index
        if largest_index != index:
            self._swap(largest_index, index)
            self._heapify(largest_index, size)

    def delete_element_at_index(self, index):
        """
        Remove the element at the specified index
        """
        if index >= self.length():
            return

        self.heap[index] = float("inf")
        self.swim_up(index + 1)
        self.extract_root()

    def _swim_up(self, index):
        """
        Method to swim up if the children are greater the root
        Args:
            index: Index of the children
            (Here we need to pass 1 based index instead of 0 based index
            so that it will be easy for us to find the parent)
        Example:
                            6
                       5        4
                   3        2       1
            In the above heap root will be self.heap[0]
            consider elements 5,4 are in respective index 2,3 the parent node
            will be (children_index/2) - 1 = (2-1) - 1 => 0
        """
        if index == 1:
            return
        parent = (index // 2)
        if self.heap[parent - 1] > self.heap[index - 1]:
            return
        self._swap(parent - 1, index - 1)
        self._swim_up(index=parent)


class MinHeap(BinaryHeap):
    def __init__(self, heap=[]):
        super(self.__class__, self).__init__(heap=heap)

    def _heapify(self, index, size):
        """
        Brief:
            Private method to shift-up the smallest number
        Args:
            heap: Unprocessed Array
            index: Index to start
            size: Size of the array
        """
        l_index = self._left_child_index(index)
        r_index = self._right_child_index(index)
        largest_index = index
        if l_index < size and self.heap[l_index] < self.heap[index]:
            largest_index = l_index
        if r_index < size and self.heap[r_index] < self.heap[largest_index]:
            largest_index = r_index
        if largest_index != index:
            self._swap(largest_index, index)
            self._heapify(largest_index, size)

    def delete_element_at_index(self, index):
        """
        Remove the element at the specified index
        """
        if index >= self.length():
            return

        self.heap[index] = float("-inf")
        self.swim_up(index + 1)
        self.extract_root()

    def _swim_up(self, index):
        """
        Method to swim up if the children are smaller the root
        Args:
            index: Index of the children
            (Here we need to pass 1 based index instead of 0 based index
            so that it will be easy for us to find the parent)
        Example:
                            1
                       2		3
                   4		5		6
            In the above heap root will be self.heap[0]
            consider elements 2,3 are in respective index 2,3 the parent node
            will be (children_index/2) - 1 = (2-1) - 1 => 0
        """
        if index == 1:
            return
        parent = (index // 2)
        if self.heap[parent - 1] < self.heap[index - 1]:
            return
        self._swap(parent - 1, index - 1)
        self._swim_up(index=parent)





