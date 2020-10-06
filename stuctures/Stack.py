class Person:
    def __init__(self, priority, value):
        self._priority = priority
        self._value = value

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def getPriority(self):
        return self._priority

    def setPriority(self, priority):
        self._priority = priority

    def __str__(self):
        return "p:{}, v:{}".format(self._priority, self._value)


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
