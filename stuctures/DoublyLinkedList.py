class Node(object):
    def __init__(self, data, Next=None, Previous=None):
        self.data = data
        self.next = Next
        self.previous = Previous

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

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
            newNode.setPrevious(self.tail)
            self.tail = newNode

    def topBack(self):
        if self.tail is None:
            raise Exception("Empty list")
        else:
            return self.tail.getData()

    def popBack(self):
        if self.head is None:
            raise Exception("Empty list")
        else:
            self.tail.getPrevious().setNext(None)
            self.tail = self.tail.getPrevious()

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
                if currNode is None:
                    raise Exception("No such data")
                    break
                elif currNode.getData() == data:
                    prevNode = currNode.getPrevious()
                    if self.tail == currNode:
                        self.tail = prevNode
                        prevNode.setNext(None)
                    else:
                        nextNode = currNode.getNext()
                        prevNode.setNext(nextNode)
                        nextNode.setPrevious(prevNode)
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

        else:
            newNode = Node(data)
            nextNode = currNode.getNext()
            currNode.setNext(newNode)
            newNode.setNext(nextNode)

    def size(self):
        currNode = self.head
        currPos = 0
        while currNode:
            currNode = currNode.next
            currPos += 1
        return currPos

    def __str__(self):
        curr = self.head
        res = ""
        while curr:
            res += " " + str(curr.getData())
            curr = curr.getNext()
        return res
