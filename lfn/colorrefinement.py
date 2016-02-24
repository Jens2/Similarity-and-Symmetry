from graphImplementations.fastgraphs import *
from util.graphIO import *
from util.graphutil import *
from copy import deepcopy

def colorref(G):
    #
    # Create a list which contains the colour number as the index with a list of vertices which all have the specified colour.
    # Also keep track of the highest known number
    mapofcolourlists = dict()
    highestDeg = - 1
    changed = True
    for v in G.V():
        if highestDeg < v.getColornum():
            highestDeg = v.getColornum()
        if mapofcolourlists.get(v.getColornum()) is not None:
            oldList = mapofcolourlists.get(v.getColornum())
            oldList.append(v)
            mapofcolourlists[v.getColornum()] = oldList
        else:
            newList = [v]
            mapofcolourlists[v.getColornum()] = newList
    buffer = mapofcolourlists
    # De colour refinement:
    while changed:

        changed = False
        mapofcolourlists = deepcopy(buffer)

        for key in mapofcolourlists.keys():
            colourlist = buffer[key]

            if len(colourlist) > 1:
                u = colourlist[0]
                changelist = []
                for v in colourlist[1:]:
                    if not checkNeighbourhood(u,v):
                        changed = True
                        colourlist.remove(v)
                        changelist.append(v)
                        # Voeg de afwijkende vertices toe aan een nieuwe lijst in de buffer map
                        if buffer.get(highestDeg + 1) is not None:
                            oldList = buffer.get(highestDeg + 1)
                            oldList.append(v)
                            buffer[highestDeg + 1] = oldList
                        else:
                            newList = [v]
                            buffer[highestDeg + 1] = newList
                for v in changelist:
                    v.updateColornum(highestDeg + 1)
                if changed:
                    highestDeg += 1
    return G
    # Voor wanneer we de map met kleuren willen returnen ipv een graph
    # return buffer

def checkNeighbourhood(u, v):
    nodedone = []
    for node in u.nbs():
        done = False
        for neighbour in v.nbs():
            if node.getColornum() == neighbour.getColornum() and neighbour not in nodedone:
                nodedone.append(neighbour)
                done = True
                break
        if not done:
            return False
    return True
"""
Voor het testen van een graph lijst en schrijven naar dot files
"""

GL, options = loadgraph('colorref_smallexample_4_16.grl', FastGraph, True)
i = 4
NGL = []
# for graph in GL:
#     writeDOT(graph, str(i) + ".dot")
#     i += 1
writeDOT(disjointunion(GL[0], GL[2]), "aaaa.dot")
# print(colorref(GL[0]))
# for graph in GL:
#     NGL.append(colorref(graph))
#     writeDOT(colorref(graph), str(i) + ".dot")
#     i += 1
# writefile = open("hoi.dot", 'wt')
# def writeln(S):
#     writefile.write(S + '\n')
# writegraphlist(NGL, writeln,options)
