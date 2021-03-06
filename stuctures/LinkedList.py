class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return "Node:{}".format(self._data)

    def getNext(self):
        return self._next

    def setNext(self, newNext):
        self._next = newNext

    def getData(self):
        return self._data

    def setData(self, newData):
        self._data = newData


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = self.head

    def pushFront(self, data):
        newNode = Node(data)
        if self.head == self.tail is None:
            self.head = self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def topFront(self):
        if self.head is None:
            raise Exception("Empty list")
        else:
            return self.head.getData()

    def popFront(self):
        if self.head is None:
            raise Exception("Empty list")
        else:
            self.head = self.head.getNext()

    def pushBack(self, data):
        newNode = Node(data)
        if self.head == self.tail is None:
            self.head = self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode

    def topBack(self):
        if self.head is None:
            raise Exception("Empty list")
        else:
            return self.tail.getData()

    def popBack(self):
        if self.head is None:
            raise Exception("Empty list")
        else:
            curr = self.head
            while curr is not self.tail:
                curr = curr.getNext()
            curr.setNext(None)
        return curr.getData()

    def find(self, data):
        currNode = self.head
        currPos = 0
        while True:
            if currNode is None:
                return False
                break
            elif currNode.getData() == data:
                return True
                break
            else:
                currNode = currNode.getNext()
                currPos += 1

    def erase(self, data):
        currNode = self.head
        currPos = 0
        if self.head == self.tail is None:
            raise Exception("Empty list")
        elif self.head.getData() == data:
            self.popFront()
        else:
            while True:
                if currNode is None or currNode.getNext() is None:
                    raise Exception("No such data")
                    break
                elif currNode.getNext().getData() == data:
                    currNode.setNext(currNode.getNext().getNext())
                    if currNode.getNext() == self.tail:
                        self.tail = currNode
                    return True
                    break
                else:
                    currNode = currNode.getNext()
                    currPos += 1

    def empty(self):
        return self.head == self.tail is None

    def insert(self, pos, data):
        currNode = self.head
        currPos = 0
        while currPos < pos - 1:
            if currNode is None or currNode.getNext().getNext() is None:
                raise Exception("No such index")
            currNode = currNode.getNext()
            currPos += 1

        newNode = Node(data)
        nextNode = currNode.getNext()
        currNode.setNext(newNode)
        newNode.setNext(nextNode)

    def size(self):
        currNode = self.head
        currPos = 0
        while currNode:
            currNode = currNode.getNext()
            currPos += 1
        return currPos

    def __str__(self):
        curr = self.head
        res = ""
        while curr:
            res += " " + str(curr.getData())
            curr = curr.getNext()
        return res

    def __iter__(self):
        return self

    def __next__(self):
        current = self.curr
        if current is None:
            raise StopIteration
        self.curr = current.getNext()
        return current
        