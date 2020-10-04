import csv
from stuctures.Queue import Queue

test = Queue()
with open('../data/MOCK_DATA.csv') as file:
    csv = csv.reader(file, delimiter=',')
    for row in file:
        test.enqueue(row.replace("\n", ""))

test.print()
print(test.dequeue())
print(test.size())


