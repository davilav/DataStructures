import csv
from stuctures.LinkedList import LinkedList

test = LinkedList()
with open('../data/MOCK_DATA.csv') as file:
    csv = csv.reader(file, delimiter=',')
    for row in file:
        test.pushFront(row)
test2 = LinkedList()
for i in range(11):
    test2.pushBack(i)
test2.popBack()
# print(test)
print(test2.size())
