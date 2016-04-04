############################################
############# Union         ################
############################################
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

    yRoot.parent = xRoot

    print(x.number, y.number , ">> union" )


class node():
    def set(self, number):
        self.parent = self
        self.number = number
        return self

class edge():
    def set(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        return self

############################################
############# InsertionSort ################
############################################

def insertionSort(arr):
    for i in range(1, len(arr)):
        index= i
        while index!=0:
            if arr[index].weight < arr[index-1].weight:
                temp = arr[index]
                arr[index]= arr[index-1]
                arr[index-1] = temp
                index = index-1
                #print(arr)
            else :
                break

############################################
############# KruskalAlgorithm #############
############################################
def kruskal(edge_list, nodes):
    # sort by weight using insertion sort
    insertionSort(edge_list)

    for edge in edges:
        print( edge.src, edge.dest, edge.weight)

    for edge in edge_list:
        union(nodes[edge.src], nodes[edge.dest])


#  make edge list
edges = []
edges.append(edge().set(0, 1, 4))
edges.append(edge().set(0, 7, 8))
edges.append(edge().set(1, 2, 8))
edges.append(edge().set(1, 7, 11))
edges.append(edge().set(2, 3, 7))
edges.append(edge().set(2, 5, 4))
edges.append(edge().set(2, 8, 2))
edges.append(edge().set(3, 4, 9))
edges.append(edge().set(3, 5, 14))
edges.append(edge().set(4, 5, 10))
edges.append(edge().set(5, 6, 2))
edges.append(edge().set(6, 7, 1))
edges.append(edge().set(6, 8, 6))
edges.append(edge().set(7, 8, 7))

# make node
nodes = list(map(lambda x:MakeSet(x), range(9)))


kruskal(edges, nodes)