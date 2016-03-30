# set 만들기
def MakeSet(number):
    return node().set(number)

# root 찾기
def find(x):
    if x.parent.number == x.number:
        return x
    else:
        return find(x.parent)

def union(x, y):
    xRoot = find(x)
    yRoot = find(y)
    xRoot.parent = yRoot


class node():
    def set(self, number):
        self.parent = self
        self.number = number
        return self

# 셋을 만든다
sets = list(map(lambda x:MakeSet(x), range(10)))
for i in range(len(sets)):
    print(sets[i].number, sets[i].parent)

for i in range(0, 4):
    union(sets[i], sets[i+1])

for i in range(5, len(sets)-1):
    union(sets[i], sets[i+1])

for i in range(len(sets)):
    print(i ," parent -> ", find(sets[i]).number)