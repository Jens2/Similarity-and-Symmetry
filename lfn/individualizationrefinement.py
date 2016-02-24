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
            if int(str(vertex.getLabel())) < length/2:
                D.append(vertex)
            else:
                I.append(vertex)
    print(D)
    print(I)
    # return D, I
    countIsomorphism(D, I, numberOfVertices, dict)
#

def countIsomorphism(D, I, numberOfVertices, dict):
    if not isBalanced(D, I, numberOfVertices):
        return 0
    if isBijection(dict):
        return 1

    colorclass = None
    for key in dict.keys():
        if len(dict.get(key)) >= 4:
            colorclass = dict.get(key)
            break
    x = None
    for vertex in colorclass:
        if vertex.getLabel() < numberOfVertices/2:
            x = vertex
            break
    num = 0
    for vertex in colorclass:
        if vertex.getLabel() >= numberOfVertices/2:
            # num += countIsomorphism()










    # TODO implement

def isBalanced(D, I, numberOfVertices):
    counter = 0
    for key in dict.keys():
        for vertex in dict.get(key):
            if int(str(vertex.getLabel())) < numberOfVertices/2:
                counter+=1
            else:
                counter-=1
    print(counter == 0)
    return counter == 0


def isBijection(dict):
    for key in dict.keys():
        if len(dict.get(key)) != 2:
            return False
    return True


    pass # TODO implement

GL, options = loadgraph('testGraphs\colorref_smallexample_4_7.grl', FastGraph, True)
dict, numberOfVertices = colorref(disjointunion(GL[0], GL[1]))
individualizationref(dict, numberOfVertices)