import csv
from stuctures.DoublyLinkedList import DoublyLinkedList

test = DoublyLinkedList()
print(test.empty())
with open('../data/MOCK_DATA.csv') as file:
    csv = csv.reader(file, delimiter=',')
    for row in file:
        test.pushBack(row.replace('\n', ''))

print(test)
print(test.insert(5, "Babyface7u7"))
print(test)
print(test.empty())
print(test.size())
