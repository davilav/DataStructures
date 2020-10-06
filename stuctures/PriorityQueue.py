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
            res = self.stack.top()
            stack2 = Stack()
            print(res)
            while (res is not None) and int(res.getPriority() >= priority):
                stack2.push( res )
                self.stack.pop()
                res = self.stack.top()
            self.stack.push(Person(priority, value))
            while not stack2.empty():
                self.stack.push(stack2.pop())



    def extract(self):
        return self.stack.pop()


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(2, 9)
    myQueue.insert(3, 8)
    myQueue.insert(4, 2)
    myQueue.insert(4, 2)
    myQueue.insert(1, 7)
    myQueue.insert(10, 7)

    print(myQueue.stack)
    myQueue.extract()
    print(myQueue.stack)