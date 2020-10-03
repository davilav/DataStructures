class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, elt):
        self.queue.append(elt)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        self.queue = []

    def peek(self):
        return self.queue[0]

    def print(self):
        s = ""
        for i in self.queue:
            s = s+"{}".format(i)
        print(s)
        return s

