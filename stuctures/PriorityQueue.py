from stuctures.Stack import Stack
from stuctures.Stack import Person


class PriorityQueue(object):
    stack = Stack()
    stack_lis = Stack()

    def __init__(self):
        self.stack.__init__()

    def __str__(self):
        return self.stack.__str__()

    def isEmpty(self):
        return self.stack.empty()

    def insert(self, priority, value):
        if self.stack.empty():
            self.stack.push(Person(priority, value))
        else:
            lis = []
            res = self.stack.top()
            while res.getPriority() >= priority and res is not None:
                lis.append(self.stack.pop())
            self.stack.push(Person(priority, value))
            for i in lis:
                self.stack.push(i)

    def extract(self):
        return self.stack.pop()


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(2, 9)
    myQueue.insert(3, 8)
    myQueue.insert(4, 6)
    myQueue.insert(5, 7)
    print(myQueue.stack)
    print(myQueue.extract())
    print(myQueue.stack)
