import csv
from stuctures.LinkedList import LinkedList

test = LinkedList()
with open('../data/MOCK_DATA.csv') as file:
    csv = csv.reader(file, delimiter=',')
    for row in file:
        test.pushFront(row.replace('\n', ''))
print(test)
test.insert(15, "Andrés")
print(test)
print(test.erase("Andrés"))

print(test)
