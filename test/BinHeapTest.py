from stuctures.BinaryHeap import MaxHeap

binTree = MaxHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
res = binTree.elements()


print("Here")
for i in range(1, len(res)+1):
    try:
        pos = i-1
        print(f"node {i}:{res[pos]}")
        print(f"left node {2*pos+1}:{res[2*pos+1]}")
        print(f"right node {2*pos+2}:{res[2*pos+2]}")
    except:
        pass