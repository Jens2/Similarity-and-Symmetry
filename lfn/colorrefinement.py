from graphImplementations.fastgraphs import graph

def colorref(G):
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