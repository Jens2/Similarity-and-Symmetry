from lfn.colorrefinement import *
from util import *
from time import time

def individualizationref(dict, numberOfVertices):
    arrays = dict.values()
    result = []
    for array in arrays:
        for element in array:
            result.append(element)
    length = len(result)
    D = []
    I = []
    for key in dict.keys():
        vertices = dict.get(key)
        for vertex in vertices:
            if vertex.getLabel() < length//2:
                D.append(vertex)
            else:
                I.append(vertex)
    # print(D)
    # print(I)
    # return D, I
    print(countIsomorphism(D, I, numberOfVertices, dict))
#

def countIsomorphism(D, I, numberOfVertices, dict, nodeList=-1):
    if nodeList == -1:
        nodeList = []
    if not isBalanced(dict, numberOfVertices):
        return 0
    if isBijection(dict):
        return 1
    num = 0
    highestDeg = -1
    for key in dict.keys():
        if key > highestDeg:
            highestDeg = key

    for key in dict.keys():
        if len(dict.get(key)) >= 4:
            colorclass = dict.get(key)
            for node in colorclass:
                if node.getLabel() < numberOfVertices//2 and node not in nodeList:
                    x = node
                    nodeList.append(x)
                    dictionary = deepCopyMap(dict)
                    for secondNode in colorclass:
                        if secondNode.getLabel() >= numberOfVertices//2:
                            # print(x.getLabel())
                            dictionary2 = deepCopyMap(dictionary)
                            dictionary2.get(key).remove(secondNode)
                            dictionary2.get(key).remove(x)

                            x.setColornum(highestDeg + 1)
                            secondNode.setColornum(highestDeg + 1)
                            newColourClass = [x, secondNode]
                            dictionary2[highestDeg + 1] = newColourClass
                            highestDeg += 1
                            # D.append(x)
                            # I.append(node)
                            # print(dictionary)
                            dictionary2 = colouring(dictionary2)
                            # print(dictionary)
                            count = countIsomorphism(D, I, numberOfVertices, dictionary2, nodeList)
                            # print(count)
                            # print(node.getLabel())
                            num += count
                            # print("num = " + str(num))
    return num












    # TODO implement

def isBalanced(dict, numberOfVertices):
    counter = 0
    for key in dict.keys():
        for vertex in dict.get(key):
            if vertex.getLabel() < numberOfVertices//2:
                counter+=1
            else:
                counter-=1
    return counter == 0


def isBijection(dict):
    for key in dict.keys():
        if len(dict.get(key)) != 2:
            return False
    return True


    pass # TODO implement

GL, options = loadgraph('testGraphs\\cographs1.grl', FastGraph, True)
startLoading = time()
graph1 = loadgraph('testGraphs\\threepaths1280.gr', FastGraph)
graph2 = loadgraph('testGraphs\\threepaths1280.gr', FastGraph)
endLoading = time()
print("Done loading graph: " + str(endLoading - startLoading))
# dict, numberOfVertices = colorref(disjointunion(GL[1], GL[3]))
startUnion = time()
graphUnion = disjointunion(graph1, graph2)
endUnion = time()
print("Done getting disjoint union: " + str(endUnion - startUnion))
startColour = time()
dict, numberOfVertices = colorref(graphUnion)
endColour = time()
print("Colouring took: " + str(endColour - startColour) + " sec")
start = time()
individualizationref(dict, numberOfVertices)
end = time()
print("Time was: " + str(end - start))
