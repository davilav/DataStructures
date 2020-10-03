import csv
from stuctures.Stack import Stack

test = Stack()
print(test.empty())
with open('../data/MOCK_DATA.csv') as file:
    csv = csv.reader(file, delimiter=',')
    for row in file:
        test.push(row)
print(test)
print(test.top())
print(test.pop())
test.push("David")
print(test.size())
print(test.empty())
