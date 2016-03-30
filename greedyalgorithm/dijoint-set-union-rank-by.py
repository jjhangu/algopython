# make set
def MakeSet(number):
    return node().set(number)

# find root
def find(x):
    if x.parent.number == x.number:
        return x
    else:
        return find(x.parent)

# merge two sets
def union(x, y):
    xRoot = find(x)
    yRoot = find(y)
    if xRoot == yRoot:
        return

    if xRoot.rank < xRoot.rank:
        xRoot.parent = yRoot;
    elif xRoot.rank > yRoot.rank:
        yRoot.parent = xRoot
    else:
        yRoot.parent = xRoot
        xRoot.rank = xRoot.rank +1

def find(x):
    print(x.number)
    if x.parent.number == x.number:
        return x
    else:
        print(x.number, "->", x.parent.number)
        return find(x.parent)

class node():
    def set(self, number):
        self.parent = self
        self.number = number
        self.rank = 0
        return self

# make set
sets = list(map(lambda x:MakeSet(x), range(10)))
for i in range(len(sets)):
    print(sets[i].number, sets[i].parent)

union(sets[1], sets[2])
union(sets[2], sets[3])
union(sets[4], sets[5])
union(sets[3], sets[5])

for i in range(1, 6):
    print(" reuslt",i, find(sets[i]).number)

