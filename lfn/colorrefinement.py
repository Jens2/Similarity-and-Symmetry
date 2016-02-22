from graphImplementations.fastgraphs import graph
import graphImplementations.basicgraphs

def colorref(G):
    a = dict()
    for v in G.V():
        a[v] = 1
    i = 0

def checkNeighbourhood(u, v):
    if len(u.nbs()) == len(v.nbs()):
        for n in u.nbs():
            if n not in v.nbs():
                return False
        return True
    else:
        return False

