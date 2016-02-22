from graphImplementations.fastgraphs import graph

def colorref(G):
    listofcolours = []
    #
    # create a list which contains the colour number as the index with a list of vertices with the specified colour.
    #
    for v in G.V():
        if listofcolours[v.getDegree] is not None:
            listofcolours.insert(v.getDegree, listofcolours[v.getDegree].append(v))
        else:
            listofcolours.insert(v.getDegree, list().append(v))
    i = 0
    # while not done

    return -1



# Checks for equality of neighbours
def checkNeighbourhood(u, v):
    if len(u.nbs()) == len(v.nbs()):
        for n in u.nbs():
            if n not in v.nbs():
                return False
        return True
    else:
        return False

def checkDegree(u, v):
    return len(u.getDegree()) == len(v.getDegree())