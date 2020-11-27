import csv
from stuctures.HashTables import HashTable
from test.TextManager import TextManager
from timeit import default_timer

if __name__ == '__main__':
    hash = HashTable(100)
    txtMan = TextManager()
    res = txtMan.reader("../data/mock_csv100.csv")
    # Primero importen from timeit import default_timer
    for i in range(10):
        pass
    # Funcion a probar
    c = 0
    for i in res.splitlines():
        print(c)
        c += 1
        key, value = i.split()
        hash.insert(key, value)
    start = default_timer()
    hash.find("")
    end = default_timer()
    print(str(end - start).replace(".", ","))

