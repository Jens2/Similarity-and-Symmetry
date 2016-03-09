from lfn.colorrefinement import *
from util import *

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

def countIsomorphism(D, I, numberOfVertices, dict, nodeList=[]):
    if not isBalanced(dict, numberOfVertices):
        return 0
    if isBijection(dict):
        print("hoi")
        return 1
    colorclass = None
    colorChosen = False
    lastKey = None
    highestDeg = -1
    for key in dict.keys():
        if len(dict.get(key)) >= 4 and not colorChosen:
            colorclass = dict.get(key)
            lastKey = key
            colorChosen = True
        if key > highestDeg:
            highestDeg = key

    num = 0
    if colorclass is not None:
        for node in colorclass:
            if node.getLabel() < numberOfVertices//2 and node not in nodeList:
                x = node
                nodeList.append(x)
                break
        dictionary = deepCopyMap(dict)
        for node in colorclass:
            if node.getLabel() >= numberOfVertices//2:
                # print(x.getLabel())
                dictionary.get(lastKey).remove(node)
                dictionary.get(lastKey).remove(x)

                x.updateColornum(highestDeg + 1)
                node.updateColornum(highestDeg + 1)
                newColourClass = [x, node]
                dictionary[highestDeg + 1] = newColourClass
                # D.append(x)
                # I.append(node)
                dictionary = colouring(dictionary)
                print(dictionary)
                count = countIsomorphism(D, I, numberOfVertices, dictionary, nodeList)
                print(count)
                num += count
                print("num = " + str(num))
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

GL, options = loadgraph('testGraphs\\torus24.grl', FastGraph, True)
dict, numberOfVertices = colorref(disjointunion(GL[0], GL[3]))
individualizationref(dict, numberOfVertices)