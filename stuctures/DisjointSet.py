class Node:
    def __init__(self, data):
        self.data = str(data)
        self.link = self
        self.size = 1

    def clear(self):
        self.link = self
        self.size = 1

class DisjointSet:
    def __init__(self, lst):
        self.verticies = {}
        self.size = len(lst)
        self.components = self.size

        for l in lst:
            n = Node(l)
            self.verticies[str(l)] = n

    # Simply prints the set for bug testing.
    def print(self):
        for v in self.verticies.values():
            print(v.data + ':', v.link.data)
        print("Number of connected components:", self.components)

    def find(self, data):
        try:
            node = self.verticies[str(data)]
            path = []
            while node.link != node:
                path.append(node)
                node = self.verticies[str(node.link.data)]
            for v in path:
                v.link = node
            return str(node.data)
        except KeyError:
            print('Invalid Key')
            return None

    def union(self, a, b):
        try:
            rootA = self.verticies[self.find(a)]
            rootB = self.verticies[self.find(b)]
            if rootA.size >= rootB.size:
                rootB.link = rootA
                rootA.size+= rootB.size
            else:
                rootA.link = rootB
                rootB.size+= rootA.size
            self.components-=1
        except KeyError:
            print('Invalid Key')
            return
    def number(self, data):
        try:
            return self.verticies[self.find(data)].size
        except KeyError:
            print('Invalid Key')
            return 0