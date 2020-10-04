import csv
from timeit import default_timer
from stuctures.Stack import Stack

test = Stack()
print(test.empty())
with open('../data/MOCK_DATA.csv') as file:
    csv = csv.reader(file, delimiter=',')
    for row in file:
        test.push(row.replace("\n", ""))

start = default_timer()
test.size()
end = default_timer()
print((end - start), "Seconds")
