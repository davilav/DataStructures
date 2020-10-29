import csv
from stuctures.LinkedList import LinkedList

test = LinkedList()
'''
with open('../data/MOCK_DATA.csv') as file:
    csv = csv.reader(file, delimiter=',')
    for row in file:
        test.pushFront(row.replace('\n', ''))
'''

for i in range(10):
    test.pushBack(i)

for i in test:
    print("i:", i)

#print(test)
