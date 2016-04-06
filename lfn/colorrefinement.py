from util.graphutil import *
from time import time

def colorref(G, onlyInit=False):
    #
    # Create a list which contains the colour number as the index with a list of vertices which all have the specified colour.
    # Also keep track of the highest known number
    mapofcolourlists = dict()
    highestDeg = - 1
    for v in G.V():
        if highestDeg < v.get_color_num():
            highestDeg = v.get_color_num()
        if mapofcolourlists.get(v.get_color_num()) is not None:
            oldList = mapofcolourlists.get(v.get_color_num())
            oldList.append(v)
            mapofcolourlists[v.get_color_num()] = oldList
        else:
            newList = [v]
            mapofcolourlists[v.get_color_num()] = newList
    if onlyInit:
        return mapofcolourlists, highestDeg, len(G.V())
    return colouring(mapofcolourlists, highestDeg), len(G.V())

def colouring(mapofcolourlists, highestDeg=-1):
    changed = True
    buffer = mapofcolourlists
    if highestDeg == -1:
        for key in mapofcolourlists.keys():
            if key > highestDeg:
                highestDeg = key
    # De colour refinement:
    while changed:

        changed = False
        mapofcolourlists = deepCopyMap(buffer)

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
                    v.set_color_num(highestDeg + 1)
                if changed:
                    highestDeg += 1
    return buffer

def deepCopyMap(mapc):
    result = dict()
    for key in mapc.keys():
        result[key] = mapc[key]
    return result

def checkNeighbourhood(u, v):
    nodedone = []
    for node in u.nbs():
        done = False
        for neighbour in v.nbs():
            if node.get_color_num() == neighbour.get_color_num() and neighbour not in nodedone:
                nodedone.append(neighbour)
                done = True
                break
        if not done:
            return False
    return True

"""
Voor het testen van een graph lijst en schrijven naar dot files
"""

# GL, options = loadgraph('testGraphs\\colorref_smallexample_4_7.grl', FastGraph, True)
# graphUnion = disjointunion(GL[1], GL[3])
# colorref(graphUnion)
# writeDOT(graphUnion, "aaa.dot")
# GL, options = loadgraph('testGraphs\\colorref_smallexample_4_7.grl', FastGraph, True)
# graphUnion2 = disjointunion(GL[1], GL[3])
# print(colorref(graphUnion))
# # getColoring2(graphUnion2).print()
# writeDOT(graphUnion2, "aab.dot")


# i = 0
# NGL = []
# for graph in GL:
#     writeDOT(graph, str(i) + ".dot")
#     i += 1
# writeDOT(colorref(disjointunion(GL[0], GL[1])), "aaaa.dot")
# print(colorref(GL[0]))
# for graph in GL:
#     NGL.append(colorref(graph))
#     writeDOT(colorref(graph), str(i) + ".dot")
#     i += 1
# writefile = open("hoi.dot", 'wt')
# def writeln(S):
#     writefile.write(S + '\n')
# writegraphlist(NGL, writeln,options)
