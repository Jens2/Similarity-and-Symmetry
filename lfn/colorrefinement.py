from util.graphutil import *

def colorref(G):
    #
    # Create a list which contains the colour number as the index with a list of vertices which all have the specified colour.
    # Also keep track of the highest known number
    mapofcolourlists = dict()
    highestDeg = - 1
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
                    v.setColornum(highestDeg + 1)
                if changed:
                    highestDeg += 1
    return buffer

def deepCopyMap(mapc):
    result = dict()
    for key in mapc.keys():
        result[key] = mapc.get(key)
    return result

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


def identicalNeighbourhoods(u, v):
    u_neighbourhood = [w.getColornum() for w in u.nbs()]
    v_neighbourhood = [w.getColornum() for w in v.nbs()]
    return u_neighbourhood == v_neighbourhood

class coloring:

    def __init__(self):
        self.__colors = dict()

    # def put(self, v):
    #     if self.__colors.get(v.getColornum) is not None:
    #         self.__colors[v.getColornum].append(v)
    #     else:
    #         self.__colors[v.getColornum] = []
    #         self.__colors[v.getColornum].append(v)

    def put(self, color, v):
        v.setColornum(color)
        if self.__colors.get(color) is not None:
            self.__colors[color].append(v)
        else:
            self.__colors[color] = []
            self.__colors[color].append(v)

    def remove(self, v):
        self.__colors[v.getColornum()].remove(v)

    def move(self, v, to):
        self.__colors[v.getColornum()].remove(v)
        self.put(to, v)

    def get(self, color):
        return self.__colors[color]

    def colors(self):
        return [c for c in self.__colors.keys() if self.__colors.get(c) is not None and len(self.__colors.get(c)) > 0]

    def deepcopy(self):
        deepcopy = coloring()
        for c in self.colors():
            deepcopy.__colors[c] = self.__colors.get(c)
        return deepcopy

    def k(self):
        k = 0
        for color_class in self.__colors.keys():
            if len(self.__colors.get(color_class)) > 0:
                k += 1
        return k

    def isStable(self):
        for color_class in self.colors():
            v = self.__colors[color_class][0]
            for u in self.__colors[color_class][1:]:
                if not identicalNeighbourhoods(u, v):
                    return False
        return True

    def isUniform(self):
        return self.k() == 1

    def isDiscrete(self):
        for color_class in self.__colors.keys():
            if len(self.__colors[color_class]) > 1:
                return False
        return True

    def print(self):
        print(self.__colors)

def getColoringByDegree(G):
    alpha = coloring()
    for v in G.V():
        alpha.put(v.getDegree(), v)
    return alpha

def getColoring(G):
    alpha = coloring()
    highestDegree = -1
    for v in G.V():
        alpha.put(v.getDegree(), v)
        if highestDegree < v.getColornum():
            highestDegree = v.getColornum()
    changed = True
    buffer = alpha
    # De colour refinement:
    while changed:
        changed = False
        alpha = buffer.deepcopy()
        for color in alpha.colors():
            colour_list = buffer.get(color)
            if len(colour_list) > 1:
                changelist = []
                u = colour_list[0]
                for v in colour_list[1:]:
                    if not identicalNeighbourhoods(u, v):
                        changed = True
                        colour_list.remove(v)
                        oldColor = v.getColornum()
                        buffer.put(highestDegree + 1 ,v)
                        changelist.append(v)
                        # buffer.move(v, highestDegree + 1)
                        v.setColornum(oldColor)
                for v in changelist:
                    # buffer.move(v, highestDegree + 1)
                    v.setColornum(highestDegree + 1)
                if changed:
                    highestDegree += 1
    return buffer

# while changed:
#
#         changed = False
#         mapofcolourlists = deepCopyMap(buffer)
#
#         for key in mapofcolourlists.keys():
#             colourlist = buffer[key]
#
#             if len(colourlist) > 1:
#                 u = colourlist[0]
#                 changelist = []
#                 for v in colourlist[1:]:
#                     if not checkNeighbourhood(u,v):
#                         changed = True
#                         colourlist.remove(v)
#                         changelist.append(v)
#                         # Voeg de afwijkende vertices toe aan een nieuwe lijst in de buffer map
#                         if buffer.get(highestDeg + 1) is not None:
#                             oldList = buffer.get(highestDeg + 1)
#                             oldList.append(v)
#                             buffer[highestDeg + 1] = oldList
#                         else:
#                             newList = [v]
#                             buffer[highestDeg + 1] = newList
#                 for v in changelist:
#                     v.setColornum(highestDeg + 1)
#                 if changed:
#                     highestDeg += 1

# G = FastGraph(7)
# G = loadgraph('bigtrees1.grl', FastGraph, True)[0][0]
# # G.addedge(G.V()[0], G.V()[5])
# # G.addedge(G.V()[1], G.V()[4])
# # G.addedge(G.V()[0], G.V()[3])
# beta = getColoring(G)
# # beta.move(G.V()[0], 6)
# # print(colorref(G))
# beta.print()
# print("Stable: " + str(beta.isStable()))
# print("Uniform: " + str(beta.isUniform()))
# print("Discrete: " + str(beta.isDiscrete()))

# writeDOT(G, "test.dot")


"""
Voor het testen van een graph lijst en schrijven naar dot files
"""

GL, options = loadgraph('testGraphs\\colorref_smallexample_4_7.grl', FastGraph, True)
graphUnion = disjointunion(GL[1], GL[3])
colorref(graphUnion)
writeDOT(graphUnion, "aaa.dot")
GL, options = loadgraph('testGraphs\\colorref_smallexample_4_7.grl', FastGraph, True)
graphUnion2 = disjointunion(GL[1], GL[3])
print(colorref(graphUnion))
getColoring(graphUnion2).print()
writeDOT(graphUnion2, "aab.dot")


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
