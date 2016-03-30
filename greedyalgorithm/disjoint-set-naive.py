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
    xRoot.parent = yRoot


class node():
    def set(self, number):
        self.parent = self
        self.number = number
        return self

# make set
sets = list(map(lambda x:MakeSet(x), range(10)))
for i in range(len(sets)):
    print(sets[i].number, sets[i].parent)

# one set is 0-4 super root is 4
for i in range(0, 4):
    union(sets[i], sets[i+1])

# the otehr set is 5~9 super root is 9
for i in range(5, len(sets)-1):
    union(sets[i], sets[i+1])

# test for all nodes finding root node
for i in range(len(sets)):
    print(i ," parent -> ", find(sets[i]).number)
