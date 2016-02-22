from graphImplementations.fastgraphs import graph

def colorref(G):
    listofcolours = []
    #
    # Create a list which contains the colour number as the index with a list of vertices which all have the specified colour.
    # Also keep track of the highest known number
    highestDeg = - 1
    for v in G.V():
        if highestDeg < v.getColornum:
            highestDeg = v.getColornum
        if listofcolours[v.getColornum] is not None:
            listofcolours.insert(v.getColornum, listofcolours[v.getColornum].append(v))
        else:
            listofcolours.insert(v.getColornum, list().append(v))
    i = 0
    # while not done.

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