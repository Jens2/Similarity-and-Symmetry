from lfn.colorrefinement import *
from util import *
from time import time
from lfn.coloringmanipulation import *

def individualizationref(dict, numberOfVertices, two=False):
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
    if not two:
        print(countIsomorphism(D, I, numberOfVertices, dict))
    else:
        print(isisomorphism(D, I, numberOfVertices, dict))

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
                            dictionary2 = colouring(dictionary2, highestDeg)

                            num += countIsomorphism(D, I, numberOfVertices, dictionary2, nodeList)
    return num

def isisomorphism(D, I, numberOfVertices, dict, nodeList=-1):
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
                            dictionary2 = coloring_refinement(dictionary2, highestDeg)

                            num += countIsomorphism(D, I, numberOfVertices, dictionary2, nodeList)
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

# GL, options = loadgraph('testGraphs\\colorref_smallexample_4_16.grl', FastGraph, True)
start = time()
graph1 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
graph2 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
graph11 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
graph22 = loadgraph('testGraphs\\almostComplete50.gr', FastGraph)
startUnion = time()
print("Done loading: " + str(startUnion - start))
# savegraph(create_complete(640), 'testGraphs\\bigComplete640.gr')
# GL, options = loadgraph('testGraphs\\colorref_smallexample_4_16.grl', FastGraph, True)
startUnion = time()
graphUnion2 = disjointunion(graph11, graph22)
print(graphUnion2)
endUnion = time()
print("******************************")
print("Time for disjointunion normal: " + str(endUnion - startUnion))
print("******************************")
startComplement = time()

graphComplement = complement(graph1)
graphComplement2 = complement(graph2)
graphUnion = disjointunion(graphComplement, graphComplement2)

endUnion = time()
print("******************************")
print("Time for complement: " + str(endUnion - startComplement))
print("******************************")
startColour = time()
dict, numberOfVertices = colorref(graphUnion2)
print(dict)
individualizationref(dict, numberOfVertices)
end = time()
# endColour = time()
print()
print("******************************")
print("Colouring complete graph: " + str(end - startColour) + " sec")
# start = time()
# individualizationref(dict, numberOfVertices)
start = time()
dict, numberOfVertices = colorref(graphUnion)
individualizationref(dict, numberOfVertices)
# colour, numberOfVertices = get_coloring(graph2)
# individualizationref(colour, numberOfVertices, True)
end = time()
print("******************************")
print("Colouring complement graph: " + str(end - start))
# print(dict)
# print(colour)
