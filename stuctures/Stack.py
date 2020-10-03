class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.stack == []
    
    def top(self):
        return self.stack[len(self.stack) - 1]

    def __str__(self):
        s = ""
        for i in self.stack[::-1]:
            s = str(s) + " " + str(i)
        return s

