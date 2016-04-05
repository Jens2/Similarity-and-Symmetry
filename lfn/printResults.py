def printIsomorphicGraphs(ListsInList):
    print("Sets of isomorphic graphs:")
    if list[0][0] == None:
        print("No isomorphic graphs")
    else:
        for i in range(0, len(list)):
            print("[" + str(list[i][0]) + ", " + str(list[i][1]) + "]")

def printNumberAut(listsInList):
    print("Graph:   Number of automorphisms:")
    for i in range(0, len(list)):
        print(str(list[i][0]) + ":       " + str(list[i][1]))